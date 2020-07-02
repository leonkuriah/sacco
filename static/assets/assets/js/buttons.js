function searchUser(){
    var userid = document.getElementById("username").value;
    window.open("http://127.0.0.1:3000/users/people/" +userid, "_self");
}
function doLogin(){
    var myName = document.getElementById("username").value;
    var myPass = document.getElementById("password").value;
    if(myName === "admin" && myPass === "admin2019"){
        window.open("http://127.0.0.1:3000/", "_self");
    }
    else{
        window.alert('Invalid username or password. Please try again');
    }
}