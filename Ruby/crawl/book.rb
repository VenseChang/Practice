require 'nokogiri'
require 'open-uri'

# Let's try to fetch and parse HTML document

books = Nokogiri::HTML(open('http://www.books.com.tw/activity/gold66_day/?loc=activity_BK_001'))

puts "### Search for nodes by css with Bookstore"
books.css('div h1 a').each do |link|
  puts link.content
end

puts "----------------------------------------------------"
books.css('a').each do |item|
  # puts item.content
  puts "#{item.content}\n#{item.attr('href')}\n\n"
end