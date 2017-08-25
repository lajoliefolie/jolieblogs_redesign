$(document).ready(function(){
    
    function load_post_functionality(){
        $("#makepost").load("/posts/make");
        $("#userposts").load("/posts/user");
    }
    window.onload = load_post_functionality();
});