function register() {
        console.log('registerform');
        var registerform = $('#' + 'register');
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: '/register',
            data: registerform.serialize() + '&csrfmiddlewaretoken=' + csrftoken,
            success: function(message) {
                if (message =='success') {
                    alert('Registered Successfully');
                    /*document.getElementById('user11').value="";
                    document.getElementById('user22').value="";
                    document.getElementById('clg').value="";
                    document.getElementById('phone').value="";
                    document.getElementById('email').value="";
                    document.getElementById('password').value="";*/
                    location.reload();
                }
                else if(message=='Exists')
                {
                    alert("Already registered. Please Login :)")
                } 
                else 
                {
                    alert('Error occured');
                }
            },
            error: function(xhr, errmsg, err) {
                alert('Error');
            },
        });
    }

function login()
 {
        console.log('loginform');
        var registerform = $('#' + 'log');
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: '/login',
            data: registerform.serialize() + '&csrfmiddlewaretoken=' + csrftoken,
            success: function(message) {
                if (message == 'Wrong')
                 {
                    alert('Enter correct Password');    //wrong pw
                 } 
                else if(message=='Success')
                {
                 window.location="/first";
                }
                else if(message=='Enter')
                {
                    alert("Kindly Enter Details");
                }
                else if("Exists")
                {                                              //success
                    alert(" User doesn't exists.Kindly Signup");
                }       
               
            },
            error: function(xhr, errmsg, err) {
                alert('Error');
            },
        });

    }

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};