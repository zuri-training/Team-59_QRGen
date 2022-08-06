'use strict'
const urlOption = document.querySelector('.url_option');
const singleOption = document.querySelectorAll('.single_option');
const optionHeaderText = document.querySelectorAll('.option_header h6')
const textOption = document.querySelector('.text_option');
const pdfOption = document.querySelector('.pdf_option');
const eventOption = document.querySelector('.event_option');
const businessOption = document.querySelector('.business_option');
const whatsAppOption = document.querySelector('.whatsapp_option');
const imagesOption = document.querySelector('.images_option');
const emailOption = document.querySelector('.email_option');
const previewLabel = document.querySelector('.preview_label');
const optionPreview = document.querySelector('.option_preview');
const dashboardDetails = document.querySelector('.dashboard_details');
const allDashboardOption = document.querySelectorAll('.dashboard_options');
const dashboardPreviewHeader = document.querySelector('.dashboard_preview_header');
const dashboardFooter = document.querySelector('.dashboard_footer');
const dashboardFooterBtn = document.querySelector('.dashboard_footer_btn');
const codeContent = document.querySelector('.code_content');
const generatedCode = document.querySelector('.generated_code');
const nextButton = document.querySelector('.continue');
const backButton = document.querySelector('.back');

const allProgressDetails = document.querySelectorAll('.progress_details');
const allLines = document.querySelectorAll('.line')
let j = 0
allProgressDetails[j].classList.add('active');

const progressFuncForward = function(){
    allProgressDetails[j].classList.remove('active');

    j++
    allProgressDetails[j].classList.add('active');
    if(j === 1){
        allLines.forEach(function(line){
            line.classList.add('active')
        })
    }else{
        allLines.forEach(function(line){
            line.classList.remove('active')
        })
    }
}
const progressFuncBackward = function(){
    allProgressDetails[j].classList.remove('active');
    j--
    allProgressDetails[j].classList.add('active');
    if(j === 1){
        allLines.forEach(function(line){
            line.classList.add('active')
        })
    }else{
        allLines.forEach(function(line){
            line.classList.remove('active')
        })
    }
}


singleOption.forEach(function(option){
    option.addEventListener('mouseover', function(){
        option.style.backgroundColor = '#003459'
        option.style.color = 'white'
    })
    option.addEventListener('mouseout', function(){
        option.style.backgroundColor = ''
        option.style.color = '#003F6C'
    })
})

let i = 0;
const qrSectionDisplay = function(){
    if(i > 0){
        optionPreview.classList.add('hide');
        generatedCode.classList.remove('hide')
    }else{
        generatedCode.classList.add('hide')
        optionPreview.classList.remove('hide');
    }
}
allDashboardOption[i].classList.add('show');
nextButton.addEventListener('click', function() {
    allDashboardOption[i].classList.remove('show')
    i++
    allDashboardOption[i].classList.add('show');
    if(i === allDashboardOption.length-1){
        dashboardDetails.classList.add('downloadslide');
        nextButton.classList.add('hide')
    }
    progressFuncForward();
    qrSectionDisplay()
})
backButton.addEventListener('click', function(){
    allDashboardOption[i].classList.remove('show');
    i--
    allDashboardOption[i].classList.add('show');
    if(i < allDashboardOption.length-1){
        dashboardDetails.classList.remove('downloadslide');
        nextButton.classList.remove('hide')
    }
    if(i === 0){
        dashboardFooter.classList.add('hide');
        dashboardFooterBtn.classList.add('hide');
    };
    progressFuncBackward()
    qrSectionDisplay()
})


const reset = () =>{
    dashboardFooter.classList.remove('hide');
    dashboardFooterBtn.classList.remove('hide');

    backButton.classList.remove('hide')

    allDashboardOption[i].classList.remove('show');
    i++
    allDashboardOption[i].classList.add('show');
    progressFuncForward();
    qrSectionDisplay();
    document.querySelectorAll('.code_content div').forEach(function(content){
        content.classList.remove('show');
    })


}
urlOption.addEventListener('click', function(){
    reset();
    document.querySelector('.url_content').classList.add('show');
})
textOption.addEventListener('click', function(){
    reset();
    document.querySelector('.text_content').classList.add('show');

});
pdfOption.addEventListener('click', function(option){
    reset();
    document.querySelector('.pdf_content').classList.add('show');

});
eventOption.addEventListener('click', function(option){
    reset();
    document.querySelector('.event_content').classList.add('show');

});
businessOption.addEventListener('click', function(option){
    reset();
    document.querySelector('.business_content').classList.add('show');

});
whatsAppOption.addEventListener('click', function(option){
    reset();
    document.querySelector('.whatsapp_content').classList.add('show');

});
imagesOption.addEventListener('click', function(option){
    reset();
    document.querySelector('.image_content').classList.add('show');

});
emailOption.addEventListener('click', function(option){
    reset();
    document.querySelector('.email_content').classList.add('show');

});

// Triggering the upload file event
document.getElementById('pdfbtn').addEventListener('click', function(e){
    e.preventDefault()
    document.getElementById('pdffile').click()
})
document.getElementById('imgbtn').addEventListener('click', function(e){
    e.preventDefault()
    document.getElementById('imgfile').click()
})