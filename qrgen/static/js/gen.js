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
        document.querySelector('.back-button').classList.add('hide'); //NEW
    }else{
        generatedCode.classList.add('hide')
        optionPreview.classList.remove('hide');
        document.querySelector('.back-button').classList.remove('hide'); //NEW
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
    if (document.querySelector(".dynamic").classList.contains("active")) {
        alert("Option not Available yet");
      }
    else {
        reset();

        document.querySelector('.text_content').classList.add('show');
    }

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
    document.getElementById('pdffile').addEventListener('change', function(){
        // console.log(e.target.closest('form').querySelector('.placeholder'));
        e.target.innerHTML = 'File Uploaded'
        e.target.closest('form').querySelector('.placeholder').setAttribute('placeholder', 'PDF file selected')
    })
})
document.getElementById('imgbtn').addEventListener('click', function(e){
    e.preventDefault()
    document.getElementById('imgfile').click()
    document.getElementById('imgfile').addEventListener('change', function(){
        e.target.innerHTML = 'File Uploaded'
        e.target.closest('form').querySelector('.placeholder').setAttribute('placeholder', 'Image selected')
    })
})
document.getElementById('bizbtn').addEventListener('click', function(e){
    e.preventDefault()
    document.getElementById('bizfile').click()
    document.getElementById('bizfile').addEventListener('change', function(){
        e.target.innerHTML = 'File Uploaded'
        e.target.closest('form').querySelector('.placeholder').setAttribute('placeholder', 'Image selected')
    })
})

// DOWNLOAD
// const downloadOptionBtn = document.querySelector('.buttons .download_btn_option');
// const downloadOptions = document.querySelector('.download_options');
// const cancleIcon = document.querySelector('.cancel');
// const downloadBtn = document.querySelectorAll('.download_btn');


// downloadOptionBtn.addEventListener('click', function(){
//     downloadOptions.classList.add('show')
// })
// cancleIcon.addEventListener('click', function(){
//     downloadOptions.classList.remove('show')
// })
// downloadBtn.forEach(function(btn){
//     btn.addEventListener('click', function(){
//         downloadOptions.classList.remove('show')
//     })
// })
// Toggle menu
document.querySelector('.profile_icon').addEventListener('click', function(){
    document.querySelector('.profile_links').classList.toggle('show')
})

document.querySelectorAll('.profile_links a').forEach(function(tag){
    tag.addEventListener('click', function(){
        document.querySelector('.profile_links').classList.remove('show')
    })
}) 


////////////////////////QR CODE ////////////////////////////////////
const dynamicBtn = document.querySelector('.dynamic');
const staticBtn = document.querySelector('.static');

dynamicBtn.addEventListener('click', function(){
    document.querySelectorAll('.input').forEach(function(input){
        input.setAttribute('value','dynamic');
    })
    dynamicBtn.classList.add('active') 
    staticBtn.classList.remove('active') 
})
staticBtn.addEventListener('click', function(){
    document.querySelectorAll('.input').forEach(function(input){
        input.setAttribute('value','static');
    })
    staticBtn.classList.add('active') 
    dynamicBtn.classList.remove('active') 
})

///////////////////////////////// SHARE FEATURE //////////////////////////////////

const shareBtn = document.querySelector('.share_btn');
// const shareNote = document.querySelectorAll('.qr_share_del .share_del div')
shareBtn.addEventListener('click', async function(e){
    const image = e.target.closest('.dashboard_details').querySelector('.qrcode_section .qrcode_box .generated_code img');
    const shareNote = e.target.closest('.buttons').querySelector('.share_notification');
    shareNote.style.opacity = 1;
    setTimeout(function(){
        shareNote.style.opacity = 0;
    }, 3000)

    // console.log(image);
    // // ***Here is the code for converting "image source" (url) to "Base64".***
    let url = image.src
    // const getUrlExtension = (url) => {
    //   return url
    //     .split(/[#?]/)[0]
    //     .split(".")
    //     .pop()
    //     .trim();
    // }
    
    const onImageEdit = async (imgUrl) => {
    //   const imgExt = getUrlExtension(imgUrl);
      const response = await fetch(imgUrl);
      const blob = await response.blob();
      const fileArray = new File([blob], "code." + "png", {
        type: blob.type,
      });
    
      if (navigator.canShare(fileArray)) {
        try {
           await navigator.share({
            title: 'qrCodeee',
            files:[fileArray]
          })
        } catch (error) {
            console.log('cant share');
        }
      } 
    }
    onImageEdit(url)
})
// Disabling onClick of QRgenerate button
document.querySelectorAll('.generate_button').forEach(function(btn){
    btn.addEventListener('click', function(){
        btn.removeAttribute("onclick");
        btn.value = "Processing...";
    });
});