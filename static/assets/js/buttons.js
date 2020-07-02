function searchUser(){
    //var userid = document.getElementById("username").value;
    window.open("http://127.0.0.1:3000/users/", "_self");
}
function doLogin(){
    var myName = document.getElementById("username").value;
    var myPass = document.getElementById("password").value;
    if(myName==='admin' && myPass==='admin2019'){
        window.open("http://127.0.0.1:3000/", "_self");
    }
    else{
        window.alert('Invalid username or password. Please try again');
    }
}
function doHome(){
    window.open("http://127.0.0.1:3000/", "_self");
}
function doIncExp(){
    window.open("http://127.0.0.1:3000/users/incex", "_self");
}
function doSetAcc(){
    window.open("http://127.0.0.1:3000/users/newacc/", "_self");
}
function doList(){
    window.open("http://127.0.0.1:3000/users/list/", "_self");
}
function doPortal(){
    window.open("http://127.0.0.1:3000/users/login/", "_self");
}
function doMain(){
    window.open("http://127.0.0.1:3000/users/main/", "_self");
}
function doEncrypt() {
    var output = "";
    var input = document.getElementById("country").value;
    for(var i = 0; i < input.length; i++){
        output += ''+input.charCodeAt(i).toString(16);
    }
    document.getElementById("country").value = output;
}