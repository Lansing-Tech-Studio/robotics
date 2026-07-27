# frozen_string_literal: true

require 'date'
require 'yaml'

TEMPLATE_TITLES = {
  'daily-scrum'   => 'Daily Scrum',
  'meeting-notes' => 'Meeting Notes',
  'robot-design'  => 'Robot Design'
}.freeze

namespace :note do
  desc 'Scaffold a dated team note snapshot. Args: team=<slug> template=<name> [date=YYYY-MM-DD]'
  task :new do
    team_slug = ENV['team'] or abort 'Missing team=<slug>'
    template  = ENV['template'] or abort "Missing template=<name>. One of: #{TEMPLATE_TITLES.keys.join(', ')}"
    abort "Unknown template '#{template}'. One of: #{TEMPLATE_TITLES.keys.join(', ')}" unless TEMPLATE_TITLES.key?(template)

    date_str = ENV['date'] || Date.today.iso8601
    date = Date.parse(date_str) # validates

    teams = YAML.load_file(File.join(__dir__, '_data', 'teams.yml'))
    team  = teams.find { |t| t['slug'] == team_slug }
    abort "Team '#{team_slug}' not found in _data/teams.yml" unless team

    dir = File.join(__dir__, 'teams', team_slug, 'notes')
    abort "Notes directory not found: #{dir}" unless Dir.exist?(dir)

    file = File.join(dir, "#{date.iso8601}-#{template}.md")
    abort "Refusing to overwrite existing file: #{file}" if File.exist?(file)

    members_snapshot = (team['members'] || []).map do |m|
      h = { 'name' => m['name'] }
      h['role'] = m['role'] if m['role']
      h
    end

    front_matter = {
      'layout'   => 'team-note',
      'title'    => "#{team['name']} #{TEMPLATE_TITLES[template]} — #{date.iso8601}",
      'date'     => date.iso8601,
      'team'     => team_slug,
      'template' => template,
      'members'  => members_snapshot
    }

    File.write(file, "#{front_matter.to_yaml}---\n\n")
    puts "Created #{file}"
  end
end
