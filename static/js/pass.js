var a
function pass() {
    if (a == 1) {
        document.getElementById('password1').type = 'password';
        document.getElementById('pass-icon').src = 'static/img/pass-hide.png';
        a = 0;
    }
    else {
        document.getElementById('password1').type = 'text';
        document.getElementById('pass-icon').src = 'static/img/pass-hide.png';
        a = 1;
    }
}