(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

window.fbAsyncInit = function () {
    FB.init({
        appId: '{your-app-id}',
        cookie: true,  // enable cookies to allow the server to access 
        xfbml: true,  // parse social plugins on this page
        version: 'v2.8', // use graph api version 2.8
        oauth:true
    });
    checkLoginState();
};

function checkLoginState() {
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            testAPI();
        } else {
            $('#pic').empty();
            $('#status').empty().append('Please log into this app.');
        }
    });
}

function testAPI() {
    console.log('Welcome!  Fetching your information.... ');

    FB.api('/me', { locale: 'en-US', fields: 'name, email, age_range, picture' }, function (response) {
        console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-');
        console.log(response);
        console.log('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-');
        $('#status').empty().append('Hello, ' + response.name + '!<br>Thank you for logging Facebook');
        
    });
}