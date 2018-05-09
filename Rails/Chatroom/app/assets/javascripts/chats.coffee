# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://coffeescript.org/


$(document).on 'keypress', (event)->
  if event.keyCode is 13
    Cookies.set('name', event.target.value);
    event.target.value = '';
    event.preventDefault();
    window.location = "/chats/show";
