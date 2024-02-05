var b
function pass1() {
    if (b == 1) {
        document.getElementById('password2').type = 'password';
        document.getElementById('pass-icon1').src = 'static/img/pass-hide.png';
        b = 0;
    }
    else {
        document.getElementById('password2').type = 'text';
        document.getElementById('pass-icon1').src = 'static/img/pass-hide.png';
        b = 1;
    }
}