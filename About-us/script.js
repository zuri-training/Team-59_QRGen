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
       $('body').animate({ scrollTop: 0 });
       // removing smooth scroll on slide-up button click
       $('body').css("scrollBehavior", "auto");
       console.log('maybe');
   });
   $('.navbar .nav-links li a').click(function () {
       // applying again smooth scroll on menu items click
       $('body').css("scrollBehavior", "smooth");
   });
   // toggle menu/navbar
   $('.menu-btn').click(function () {
       $('.navbar .nav-links').toggleClass("active");
       $('.menu-btn i').toggleClass("active");
       console.log('yes');
   });
});

const slides = document.querySelectorAll('.profile');
const nextBtn = document.querySelector('.nextslide')
const slider = function () {
    let curSlide = 0;
    const maxSlide = slides.length - 1;
  
    //Functions
  
    const goToSlide = function (slide) {
      slides.forEach((s, i) => {
        if(i === slide){
            s.classList.add('show')
        } else{
            s.classList.remove('show')
        }
      });
    };
  
    //Next slide
    const nextSlide = function () {
      if (curSlide === maxSlide) {
        curSlide = 0;
      } else {
        curSlide++;
      }
      goToSlide(curSlide);
    };
    const init = function () {
      goToSlide(0);
    };
    init();
    ///Event handlers
    nextBtn.addEventListener('click', nextSlide);
}
slider();