#coding: utf-8
require 'open-uri'
require 'nokogiri'
require 'json'

popular = true
url = "https://www.dcard.tw/_api/forums/funny/posts?popular=#{popular}"
res = Nokogiri::HTML.parse(open(url), nil, "UTF-8")

json = JSON.parse(res.content)



json.each{ |item|
  puts """
    #{ item['forumName'] }
    #{ item['title'] }
    #{ item['excerpt'] }
    #{ item['school'] } #{ item['deparment'] }
    #{ item['commentCount'] }  comments / #{ item['likeCount'] } likes
    """
}