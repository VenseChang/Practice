# 注意事項
1. 下方圖 1-1 紅框的部分記得填測試的網址
    像我本機用 Python 測試，所以填 localhost  
    - Python 測試語法
    - 在要測試的資料夾內，用cmd執行 python -m http.server
    - 預設port為8000
    - 這邊不用填 localhost:8000，localhost即可  

    - 若是要上線的網站，記得將Domain加到紅框處

    ![](images/pic01.jpg)
    ▲ 圖 1-1

2. JavaScript 
    - ### FB.init的地方記得將 <font color="red">{your-app-id}</font>換成自己的appID
    - ### FB.api
        - ### locale 可以設定語系
            - 英文 : en-US
            - 中文 : zh-hant
        - ### fields 可填需要回傳什麼資訊，<font color="red">若沒有 fields ，則只會回傳 id 跟 name</font>

        - ### 有些資訊需要使用者授權才能取得
        - ### 有些資訊需要FB先審核過應用後方可使用&取得
3. App id
    ![](images/pic02.jpg)

## 參考資料 : 
1. [Facebook for Developers](https://developers.facebook.com/)
2. [Authority document](https://developers.facebook.com/docs/facebook-login/permissions#reference-user_status)
3. [Graph-API document](https://developers.facebook.com/docs/graph-api/reference/user) 