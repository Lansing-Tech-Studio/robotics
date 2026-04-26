# frozen_string_literal: true

# Generates per-team template pages at /teams/<slug>/templates/<template>/
# for every team in _data/teams.yml × every entry in TEMPLATES below.
# Each generated page renders the corresponding partial in
# _includes/templates/, pre-filled with the team's name, coach, and roster.
module Jekyll
  class TeamTemplatePage < Page
    def initialize(site, base, team, template)
      @site = site
      @base = base
      @dir  = File.join('teams', team['slug'], 'templates', template[:slug])
      @name = 'index.html'

      self.process(@name)
      self.data = {
        'layout'        => 'team-template',
        'team_slug'     => team['slug'],
        'template_name' => template[:slug],
        'title'         => "#{team['name']} — #{template[:title]}"
      }
      self.content = ''
    end

    # No source file on disk — skip Jekyll's attempt to read one.
    def read_yaml(*); @data ||= {}; end
  end

  class TeamTemplateGenerator < Generator
    safe true
    priority :low

    TEMPLATES = [
      { slug: 'daily-scrum',   title: 'Daily Scrum'   },
      { slug: 'meeting-notes', title: 'Meeting Notes' },
      { slug: 'robot-design',  title: 'Robot Design'  }
    ].freeze

    def generate(site)
      teams = site.data['teams'] || []
      teams.each do |team|
        next unless team['slug']
        TEMPLATES.each do |template|
          site.pages << TeamTemplatePage.new(site, site.source, team, template)
        end
      end
    end
  end
end
