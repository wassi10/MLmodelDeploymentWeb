// <!-- === Sticky Navbar === -->

window.addEventListener('scroll', function () {
  var header = document.querySelector('.header')
  header.classList.toggle('sticky', window.scrollY > 0)
})


// const sr = ScrollReveal ({
//   distance: '20px',
//   duration: 3000,
//   reset: true
// });
// sr.reveal('.header',{delay: 190, origin: 'left'});
// sr.reveal('.home, .heading',{delay: 200, origin: 'top'});
// sr.reveal('.about-img, .about-content, .education-row, .skills-content, .projects-content, form, .footer',{delay: 200, origin: 'bottom'});



// forgot pass eyeon, off
// var pass
// function resetpass() {
//   if (pass == 1) {
//     document.getElementById('password1').type = 'password';
//     document.getElementById('pass-icon').src = 'static/img/eyeon.png';
//     pass = 0;
//   }
//   else {
//     document.getElementById('password1').type = 'text';
//     document.getElementById('pass-icon').src = 'static/img/eyeoff.png';
//     pass = 1;
//   }
// }

// var pass1
// function resetpass1() {
//   if (pass1 == 1) {
//     document.getElementById('password2').type = 'password';
//     document.getElementById('pass-icon1').src = 'static/img/eyeon.png';
//     pass1 = 0;
//   }
//   else {
//     document.getElementById('password2').type = 'text';
//     document.getElementById('pass-icon1').src = 'static/img/eyeoff.png';
//     pass1 = 1;
//   }
// }