$(document).ready(function(){
      $("#login_button").click(function(){
          var username=$('#username').val();
          var password=$('#password').val();
          if((username === '' ) || (password === '')){
            $("#empty_error").show().delay(6000).fadeOut();
          }else{
          	$('#loading_msg').show();
            params = {
                'username': username,
                'password': password,
                }
             $.ajax({
                type: "POST",
                url: "/authenticateUser/",
                data: JSON.stringify(params),
                contentType: "application/json",
                success: function(res) {
                    if (res == 'authentic') {
                        console.log('success')
                        $('#loading_msg').hide();
                        window.location.href='/dashboard/'
                    } else {
                    	$('#loading_msg').hide();
                        $("#cred_error").show().delay(6000).fadeOut();
                    }
                }
            });
          }

      })
  });