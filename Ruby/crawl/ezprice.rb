require "open-uri" #open-uri 把一個網頁當一個檔案來打開 stb-lib
require "nokogiri" #解析 html gem

html = open("http://ezprice.com.tw/").read
doc = Nokogiri::HTML(html)
ans = []

doc.search('img').each do |i|
  ans << i.attr('src') #取得html img tag的src，加到ans list內
end

# 將相對路徑改成絕對路徑
temp_ans = ans.map { |url| url.match(/^http/) ? url : "http://ezprice.com.tw/#{url}" }

# 透過 wget 下載檔案到目前的資料夾
temp_ans.each { |full_url| `wget #{full_url}` }