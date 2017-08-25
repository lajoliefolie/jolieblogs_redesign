$(document).ready(function () {
    $('#login').submit(function(event){
        
        event.preventDefault(); //Won't move forward with default false action. Not good for this. Return True/False from this JS!
            
        $.getJSON("/login/process", {
            email: document.getElementById("input_email").value,
            password: document.getElementById("input_password").value
            },function(data) {
                if(!data){
                    document.getElementById("login_message").innerHTML = "Invalid login combination."
                }
                else{
                    document.getElementById("login_message").innerHTML = "Valid login!."
                }
            }
        );
    });
});