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