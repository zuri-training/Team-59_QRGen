const all = document.querySelector('#all');
const active = document.querySelector('#active');
const archive = document.querySelector('#archive');
const filterBtn = document.querySelector('.filter_btn')


all.addEventListener('click', function(){
    all.classList.add('active');
    active.classList.remove('active');
    archive.classList.remove('active');
    filterBtn.innerHTML = ''
    filterBtn.insertAdjacentHTML('afterbegin',
        `
        <button>
            <img src="./image/icon/all-icon.png" alt="">
            <p>All QR codes</p>
        </button>
        `
    )
})
active.addEventListener('click', function(){
    active.classList.add('active');
    all.classList.remove('active');
    archive.classList.remove('active');
    filterBtn.innerHTML = ''
    filterBtn.insertAdjacentHTML('afterbegin',
        `
        <button>
            <img src="./image/icon/active-icon.png" alt="">
            <p>Active QR codes</p>
        </button>
        `
    )
})
archive.addEventListener('click', function(){
    archive.classList.add('active');
    all.classList.remove('active');
    active.classList.remove('active');
    filterBtn.innerHTML = ''
    filterBtn.insertAdjacentHTML('afterbegin',
        `
        <button>
            <img src="./image/icon/archive-icon.png" alt="">
            <p>Archive QR codes</p>
        </button>
        `
    )
})

// Toggle menu
document.querySelector('.profile_icon').addEventListener('click', function(){
    document.querySelector('.profile_links').classList.toggle('show')
})

document.querySelectorAll('.profile_links a').forEach(function(tag){
    tag.addEventListener('click', function(e){
        e.preventDefault()
        document.querySelector('.profile_links').classList.remove('show')
    })
}) 

// DOWNLOAD
const downloadOptions = document.querySelector('.download_options');
const cancelIcon = document.querySelectorAll('.cancel');
const downloadBtn = document.querySelectorAll('.download_btn');

cancelIcon.forEach(function(cancel){
    cancel.addEventListener('click', function(e){
        console.log('working');
        e.target.closest('.qr_download ').querySelector('.download_options').classList.remove('show')
    })
})
downloadBtn.forEach(function(btn){
    btn.addEventListener('click', function(e){
        e.target.closest('.qr_download ').querySelector('.download_options').classList.toggle('show')
    })
})

///////////////////////////////// SHARE FEATURE //////////////////////////////////

const shareicon = document.querySelectorAll('.share');
shareicon.forEach(function(icon){
    icon.addEventListener('click', async function(e){
        const shareNote = e.target.closest('.share_del').querySelector('.share-notification');
        console.log(shareNote);
        shareNote.style.opacity = 1;
        setTimeout(function(){
            shareNote.style.opacity = 0;
        }, 3000)
        const image = e.target.closest('.saved_data').querySelector('.qr_image img');
        console.log(image);
        // ***Here is the code for converting "image source" (url) to "Base64".***
        let url = image.src
        console.log(url);
        const getUrlExtension = (url) => {
          return url
            .split(/[#?]/)[0]
            .split(".")
            .pop()
            .trim();
        }
        
        const onImageEdit = async (imgUrl) => {
          const imgExt = getUrlExtension(imgUrl);
          const response = await fetch(imgUrl);
          const blob = await response.blob();
          const fileArray = new File([blob], "search-icon." + imgExt, {
            type: blob.type,
          });
          console.log(fileArray);
        
          if (navigator.canShare(fileArray)) {
            try {
               await navigator.share({
                title: 'qrCodeee',
                files:[fileArray]
              })
              console.log('can share');
            //   output.textContent = 'Shared!'
            } catch (error) {
                console.log('cant share');
            //   output.textContent = `Error: ${error.message}`
            }
          } 
        }
        onImageEdit(url)
    })
})

