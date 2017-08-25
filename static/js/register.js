$(document).ready(function () {
    $('#register').submit(function(event){
        
        event.preventDefault(); //Won't move forward with default false action. Not good for this. Return True/False from this JS!
            
        $.getJSON("/register/process", {
            email: document.getElementById("input_email").value,
            password: document.getElementById("input_password").value,
            password_confirm: document.getElementById("input_password_confirm").value
            },function(data) {
                if(data == "pw_nomatch"){
                    document.getElementById("register_message").innerHTML = "Passwords do not match."
                }
                else if(data == "email_used"){
                    document.getElementById("register_message").innerHTML = "Email already used."
                }
                else{
                    document.getElementById("register_message").innerHTML = "Valid register!."
                }
            }
        );
    });
});