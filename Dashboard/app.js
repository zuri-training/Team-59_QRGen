'use strict'
const urlOption = document.querySelectorAll('.url_option');
const textOption = document.querySelector('.text_option');
const pdfOption = document.querySelector('.pdf_option');
const eventOption = document.querySelector('.event_option');
const previewLabel = document.querySelector('.preview_label');
const optionPreview = document.querySelector('.option_preview');
const dashboardFooter = document.querySelector('.dashboard_footer')


const reset = () =>{
    urlOption.forEach(option =>{
        option.style.background = 'none'
    })
    dashboardFooter.classList.remove('hide')
    textOption.style.background = 'none'
    pdfOption.style.background = 'none'
    eventOption.style.background = 'none'
}
urlOption.forEach(option =>{
    option.addEventListener('click', function(){
        reset();
        option.style.background = '#ACACAD';
        previewLabel.innerHTML = '';
        previewLabel.insertAdjacentHTML('afterbegin',
        `<div class="option_header">
            <img src="./img/icons/link-svgrepo-com 1.png" alt="link">
            <h6>Website URL</h6>
        </div>
        <span class="preview_line">
        </span>
        <h5>Your 
            preview will show here
        </h5>`
        );
        previewLabel.classList.remove('hide');
        optionPreview.classList.add('hide')
        console.log('k');

    })
});
textOption.addEventListener('click', function(){
    reset();
    textOption.style.background = '#ACACAD'
    previewLabel.innerHTML = '';
    previewLabel.insertAdjacentHTML('afterbegin',
    `<div class="option_header">
        <img src="./img/icons/text-svgrepo-com (1) 1.png" alt="link">
        <h6>Text</h6>
    </div>
    <span class="preview_line">
    </span>
    <h5>Your 
        preview will show here
    </h5>`
    );
    previewLabel.classList.remove('hide');
    optionPreview.classList.add('hide')
});
pdfOption.addEventListener('click', function(option){
    reset();
    pdfOption.style.background = '#ACACAD'
    previewLabel.innerHTML = '';
    previewLabel.insertAdjacentHTML('afterbegin',
    `<div class="option_header">
        <img src="./img/icons/pdf-svgrepo-com 1.png" alt="link">
        <h6>PDF</h6>
    </div>
    <span class="preview_line">
    </span>
    <h5>Your 
        preview will show here
    </h5>`
    );
    previewLabel.classList.remove('hide');
    optionPreview.classList.add('hide')
});
eventOption.addEventListener('click', function(option){
    reset();
    eventOption.style.background = '#ACACAD'
    previewLabel.innerHTML = '';
    previewLabel.insertAdjacentHTML('afterbegin',
    `<div class="option_header">
        <img src="./img/icons/Group.png" alt="link">
        <h6>Event</h6>
    </div>
    <span class="preview_line">
    </span>
    <h5>Your 
        preview will show here
    </h5>`
    );
    previewLabel.classList.remove('hide');
    optionPreview.classList.add('hide')
});