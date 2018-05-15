#coding: utf-8
require 'open-uri'
require 'nokogiri'
require "mini_magick"

def directory_exists?(directory)
  File.directory?(directory)
end

def save_origin_size urls, path
  urls.each { |full_url| `wget #{full_url} -O #{path}/#{full_url.split('sticker/')[1].sub('/ANDROID/sticker', '')}` }
end

def save_512_size urls, path
  urls.each { |full_url| 
    name = full_url.split('sticker/')[1].sub('/ANDROID/sticker', '')
    image = MiniMagick::Image.open(full_url)
    image.resize "512x512"
    image.format "png"
    image.write "#{path}/#{name}"
  }
end

def main
  root_path = "stickers"
  `mkdir #{root_path}` if !directory_exists? root_path

  for id in ARGV
    path = "#{root_path}/#{id}"
    `mkdir #{path}` if !directory_exists? path
    `mkdir #{path}/size_origin`   if !directory_exists? "#{path}/size_origin"
    `mkdir #{path}/size_512` if !directory_exists? "#{path}/size_512"

    url = "https://line.me/S/sticker/#{id}"
    res = Nokogiri::HTML.parse(open(url), nil, "UTF-8")
    
    image_urls = []
    res.search('span.mdCMN09Image').each do |i|
      image_urls << i.attr('style').sub('background-image:url(', '').sub(';compress=true);', '')
    end
    
    save_512_size    image_urls, "#{path}/size_512"
    save_origin_size image_urls, "#{path}/size_origin"

  end
  puts "Images All Saved."
end

# ----------------------------------------

main()
