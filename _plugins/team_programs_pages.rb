# frozen_string_literal: true

require 'rouge'
require 'zip'

# Generates per-team Programs pages:
#   - /teams/<slug>/programs/                — index listing every file in
#     teams/<slug>/programs/.
#   - /teams/<slug>/programs/<filename>.html — syntax-highlighted viewer for
#     each Python source file, with a download link to the raw .py file at
#     /teams/<slug>/programs/<filename>.
#
# Non-Python files in the index link directly to the raw static file so the
# browser handles them (download or inline render as appropriate).
module Jekyll
  PROGRAMS_DIR = 'programs'

  # Files we never want to surface (WSL/Windows alt-streams, OS junk, caches).
  PROGRAMS_IGNORE = [
    /:Zone\.Identifier\z/,
    /\A\./,           # dotfiles
    /\A__pycache__\z/,
    /\.pyc\z/
  ].freeze

  module ProgramsHelpers
    module_function

    def list_program_files(site_source, team_slug)
      dir = File.join(site_source, 'teams', team_slug, PROGRAMS_DIR)
      return [] unless Dir.exist?(dir)

      Dir.children(dir).reject do |name|
        path = File.join(dir, name)
        !File.file?(path) || PROGRAMS_IGNORE.any? { |re| name =~ re }
      end.sort
    end
  end

  class TeamProgramsIndexPage < Page
    def initialize(site, base, team, files)
      @site = site
      @base = base
      @dir  = File.join('teams', team['slug'], PROGRAMS_DIR)
      @name = 'index.html'

      process(@name)
      self.data = {
        'layout' => 'default',
        'title'  => "#{team['name']} — Programs"
      }

      team_url = "/teams/#{team['slug']}/"
      programs_url = "#{team_url}#{PROGRAMS_DIR}/"

      zip_name = "#{team['slug']}-programs.zip"
      zip_link = files.empty? ? '' : <<~HTML
        <p class="program-actions no-print">
          <a href="#{zip_name}" download>Download all as zip (#{zip_name})</a>
        </p>
      HTML

      rows = files.map do |name|
        is_python = name.end_with?('.py')
        href = is_python ? "#{name}.html" : name
        type_label = is_python ? 'Python' : File.extname(name).sub('.', '').upcase
        type_label = 'File' if type_label.empty?
        download_link = is_python ? %( &middot; <a href="#{name}" download>download</a>) : ''
        <<~HTML
          <li>
            <a href="#{href}">#{name}</a>
            <span class="program-meta">(#{type_label})#{download_link}</span>
          </li>
        HTML
      end

      body =
        if files.empty?
          '<p><em>No program files have been uploaded yet.</em></p>'
        else
          %(<ul class="program-list">\n#{rows.join}\n</ul>)
        end

      self.content = <<~HTML
        <h1>#{team['name']} — Programs</h1>
        <p class="no-print"><a href="#{team_url}">&larr; Back to #{team['name']}</a></p>
        #{zip_link}
        #{body}
      HTML
    end

    def read_yaml(*); @data ||= {}; end
  end

  class TeamProgramsPythonViewerPage < Page
    LEXER = Rouge::Lexers::Python.new
    FORMATTER = Rouge::Formatters::HTMLLegacy.new(line_numbers: true, css_class: 'highlight')

    def initialize(site, base, team, filename)
      @site = site
      @base = base
      @dir  = File.join('teams', team['slug'], PROGRAMS_DIR)
      @name = "#{filename}.html"

      process(@name)
      self.data = {
        'layout' => 'default',
        'title'  => "#{team['name']} — #{filename}"
      }

      source_path = File.join(base, 'teams', team['slug'], PROGRAMS_DIR, filename)
      source = File.exist?(source_path) ? File.read(source_path) : ''
      highlighted = FORMATTER.format(LEXER.lex(source))

      programs_url = "/teams/#{team['slug']}/#{PROGRAMS_DIR}/"

      self.content = <<~HTML
        <h1>#{filename}</h1>
        <p class="no-print program-actions">
          <a href="#{programs_url}">&larr; Back to Programs</a>
          &middot;
          <a href="#{filename}" download>Download #{filename}</a>
        </p>
        <div class="program-source">
          #{highlighted}
        </div>
      HTML
    end

    def read_yaml(*); @data ||= {}; end
  end

  # Static file that materializes a zip of every program file for a team
  # directly into the destination directory at write time. Avoids polluting
  # the source tree with build artifacts.
  class TeamProgramsZipFile < StaticFile
    def initialize(site, team_slug, files)
      @site = site
      @base = site.source
      @dir  = "/teams/#{team_slug}/#{PROGRAMS_DIR}"
      @name = "#{team_slug}-programs.zip"
      @collection = nil
      @relative_path = File.join(@dir, @name)
      @extname = '.zip'
      @team_slug = team_slug
      @program_files = files
    end

    def path
      File.join(@base, 'teams', @team_slug, PROGRAMS_DIR, @name)
    end

    def modified_time
      times = @program_files.map do |f|
        File.mtime(File.join(@base, 'teams', @team_slug, PROGRAMS_DIR, f))
      end
      times.max || Time.now
    end

    def write(dest)
      dest_path = File.join(dest, @dir, @name)
      FileUtils.mkdir_p(File.dirname(dest_path))

      File.delete(dest_path) if File.exist?(dest_path)
      Zip::File.open(dest_path, Zip::File::CREATE) do |zip|
        @program_files.each do |name|
          src = File.join(@base, 'teams', @team_slug, PROGRAMS_DIR, name)
          zip.add(name, src)
        end
      end
      true
    end

    def modified?; true; end
  end

  class TeamProgramsGenerator < Generator
    safe true
    priority :low

    def generate(site)
      teams = site.data['teams'] || []
      teams.each do |team|
        slug = team['slug']
        next unless slug

        files = ProgramsHelpers.list_program_files(site.source, slug)

        # Always create the index (even when empty) so the link from the team
        # page resolves to a friendly "no files yet" message.
        site.pages << TeamProgramsIndexPage.new(site, site.source, team, files)

        files.each do |filename|
          next unless filename.end_with?('.py')
          site.pages << TeamProgramsPythonViewerPage.new(site, site.source, team, filename)
        end

        # Bundle a zip of every program file (Python or otherwise) for the
        # team. Skip when there's nothing to package.
        site.static_files << TeamProgramsZipFile.new(site, slug, files) unless files.empty?
      end
    end
  end
end
