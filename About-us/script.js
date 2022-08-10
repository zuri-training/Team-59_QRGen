$(document).ready(function () {
    $(window).scroll(function () {
        // scroll-up button show/hide
        if (this.scrollY > 500) {
            $('.scroll-up-btn').addClass("show");
        } else {
            $('.scroll-up-btn').removeClass("show");
        }
    });
    // slide-up
   $('.scroll-up-btn').click(function () {
       $('html').animate({ scrollTop: 0 });
       // removing smooth scroll on slide-up button click
       $('html').css("scrollBehavior", "auto");
   });
   $('.navbar .nav-links li a').click(function () {
       // applying again smooth scroll on menu items click
       $('html').css("scrollBehavior", "smooth");
   });
   // toggle menu/navbar
   $('.menu-btn').click(function () {
       $('.navbar .nav-links').toggleClass("active");
       $('.menu-btn i').toggleClass("active");
   });
});