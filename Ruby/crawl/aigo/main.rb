require 'json'
require 'watir'
require 'nokogiri'
require 'mechanize'

def get_info(filter_competition_list)
  items = filter_competition_list.css('.col-md-12')
  items.map do |item|
    link     = item.at('a').attributes['href'].value.strip
    title    = item.at('.competition_title').children.text.strip
    subtitle = item.at('.competition_subtitle').children.text.strip.gsub("\n", '')
    company  = item.at('.competition_bottom p').children.text.strip
    
    if @info[company]
      @info[company].append(
        {
          link: link,
          title: title,
          subtitle: subtitle
        }
      )
    else
      @info[company] = [
        {
          link: link,
          title: title,
          subtitle: subtitle
        }  
      ]
    end
  end
end

@info = {}

browser = Watir::Browser.new
browser.goto('https://aigo.org.tw/ai-plus/competitions/c2019_plus')

page = Nokogiri::HTML.parse(browser.html)

total_page = page.css('ul.pagination').size

(1..total_page).each do |index|
  browser.link(text: index.to_s).click
  sleep(0.5)
  page = Nokogiri::HTML.parse(browser.html)
  get_info(page.at('div#filter_competition_list'))
  sleep(0.5)
end

File.open("./aigo.json","w") do |f|
  f.write(JSON.pretty_generate(@info))
end