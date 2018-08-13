#coding: utf-8
require 'open-uri'
require 'nokogiri'

app_id = ARGV[0]
url = "https://play.google.com/store/apps/details?id=#{app_id}"
res = Nokogiri::HTML.parse(open(url), nil, "UTF-8")

current_version = nil
res.search(".hAyfc").each{|val|
  if val.to_s.match('Current Version')
    current_version =  val.search("div span.htlgb").to_s.sub('<span class="htlgb">', '').sub('</span>', '') 
  end
}

puts current_version