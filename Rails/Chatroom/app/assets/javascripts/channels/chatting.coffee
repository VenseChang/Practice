url = window.location.href.split('chats/')[1]
if(url == 'show')
  App.chatting = App.cable.subscriptions.create "ChattingChannel",
    connected: ->
      # Called when the subscription is ready for use on the server
      if(typeof Cookies.get('name') == 'undefined' )
        window.location = '/'
      $('#messages').append('<li class="log" style="display: list-item;">Welcome to Socket.IO Chat – </li>')
      console.log messages

    disconnected: ->
      # Called when the subscription has been terminated by the server

    received: (data) ->
      # Called when there's incoming data on the websocket for this channel

    speak: ->
      @perform 'speak'
