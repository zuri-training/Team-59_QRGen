const all = document.querySelector('#all');
// const active = document.querySelector('#active');
// const archive = document.querySelector('#archive');
// const filterBtn = document.querySelector('.filter_btn')


// all.addEventListener('click', function(){
//     all.classList.add('active');
//     active.classList.remove('active');
//     archive.classList.remove('active');
//     filterBtn.innerHTML = ''
//     filterBtn.insertAdjacentHTML('afterbegin',
//         `
//         <button>
//             <img src="./image/icon/all-icon.png" alt="">
//             <p>All QR codes</p>
//         </button>
//         `
//     )
// })
// active.addEventListener('click', function(){
//     active.classList.add('active');
//     all.classList.remove('active');
//     archive.classList.remove('active');
//     filterBtn.innerHTML = ''
//     filterBtn.insertAdjacentHTML('afterbegin',
//         `
//         <button>
//             <img src="./image/icon/active-icon.png" alt="">
//             <p>Active QR codes</p>
//         </button>
//         `
//     )
// })
// Toggle menu
document.querySelector('.profile_icon').addEventListener('click', function(){
    document.querySelector('.profile_links').classList.toggle('show')
})

document.querySelectorAll('.profile_links a').forEach(function(tag){
    tag.addEventListener('click', function(e){
        // e.preventDefault()
        document.querySelector('.profile_links').classList.remove('show')
    })
}) 

// DOWNLOAD
const downloadOptions = document.querySelector('.download_options');
const cancelIcon = document.querySelectorAll('.cancel');
const downloadBtn = document.querySelectorAll('.download_btn');

cancelIcon.forEach(function(cancel){
    cancel.addEventListener('click', function(e){
        // console.log('working');
        e.target.closest('.qr_download ').querySelector('.download_options').classList.remove('show')
    })
})
downloadBtn.forEach(function(btn){
    btn.addEventListener('click', function(e){
        e.target.closest('.qr_download ').querySelector('.download_options').classList.toggle('show')
    })
})

//////////////////////////// Change title model ///////////////////////
const editicon = document.querySelectorAll('.edit_icon');
// console.log(editicon);
editicon.forEach(function(icon){
    icon.addEventListener('click', async function(e){
        e.target.closest('.qr_image').querySelector('.title_form').classList.add('show');
    })
})

const cancel = document.querySelectorAll('.modal_cancel_icon');

cancel.forEach(function(icon){
    icon.addEventListener('click', function(e){
        // console.log('working');
        e.target.closest('.title_form').classList.remove('show');
    })
})

const changeBtn = document.querySelectorAll('.change_btn');

changeBtn.forEach(function(btn){
    btn.addEventListener('click', function(e){
        // e.preventDefault()
        e.target.closest('.title_form').classList.remove('show');
    })
})

/////////////////////////////////////   CHANGE QRCODE CODE   ///////////////////////////////////////
const contentEditBtn = document.querySelectorAll('.content_edit_btn');
const editForm = document.querySelector('.edit_form');
contentEditBtn.forEach(function(btn){
    btn.addEventListener('click', function(){
        // console.log('yes');
        // console.log(editForm);
        btn.closest('.des_share_del').querySelector(".edit_form").classList.add('show');
    })
})
const cancelX = document.querySelectorAll('.content_modal_cancel');
cancelX.forEach(function(icon){
    icon.addEventListener('click', function(e){
        // console.log('working');
        e.target.closest('.edit_form').classList.remove('show');
    })
})
const changeX = document.querySelectorAll('.change_btn_x');
changeX.forEach(function(btn){
    btn.addEventListener('click', function(){
        // e.preventDefault()
        e.target.closest('.edit_form').classList.remove('show');
    })
})

// ///////////////////////////////////   DELETE POP UP   /////////////////////////////////////////

// const deleteIcon = document.querySelectorAll('.delete_icon');
// const deleteModal = document.querySelector('.delete_modal');
// const cancelB = document.querySelector('.button_section .cancelx');

// deleteIcon.forEach(function(btn){
//     btn.addEventListener('click', function(){
//         deleteModal.classList.add('show')
//     })
// })

// cancelB.addEventListener('click', function(){
//     deleteModal.classList.remove('show')
// })


///////////////////////////////// SHARE FEATURE //////////////////////////////////

const shareicon = document.querySelectorAll('.share');
// console.log(shareicon);
shareicon.forEach(function(icon){
    icon.addEventListener('click', async function(e){
        const shareNote = e.target.closest('.share_del').querySelector('.share-notification');
        // console.log(shareNote);
        shareNote.style.opacity = 1;
        setTimeout(function(){
            shareNote.style.opacity = 0;
        }, 3000)
        const image = e.target.closest('.saved_data').querySelector('.qr_image .code');
        // console.log(image);
        // ***Here is the code for converting "image source" (url) to "Base64".***
        let url = image.src
        // console.log(url);
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
        //   console.log(fileArray);
        
          if (navigator.canShare(fileArray)) {
            try {
               await navigator.share({
                title: 'qrCode',
                files:[fileArray]
              })
            //   console.log('can share');
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


// /////////////////////////////// SEARCH//////////////////////////////
// // document.querySelector('.search_btn').addEventListener('click', function(e){
// //      e.preventDefault();
// // })
// function search(){
//     let input = document.querySelector('.search').value
//     input = input.toLowerCase();
//     let x = document.querySelectorAll('.qr_image .title')
//     for (let i = 0; i < x.length; i++) {
//         console.log(x[i].closest('.saved_data'));
//         if(!x[i].innerHTML.toLowerCase().includes(input)){
//             x[i].closest('.saved_data').style.display = 'none'
//         } else{
//             x[i].closest('.saved_data').style.display = 'flex'
//         }
//     }
// }


///////////////////////////////////   DELETE POP UP   /////////////////////////////////////////
const deleteIcon = document.querySelectorAll('.delete_icon');
const deleteModal = document.querySelectorAll('.delete_modal');
const cancelB = document.querySelectorAll('.button_section .cancelx');
deleteIcon.forEach(function(btn){
    btn.addEventListener('click', function(){
        btn.closest('.saved_data').querySelector(".delete_modal").classList.add('show')
    })
})
cancelB.forEach(function(btn){
    btn.addEventListener('click', function(){
        deleteModal.forEach(function(modal){
            modal.classList.remove('show')
        })
    })
})

/////////////////////////////// SEARCH//////////////////////////////
document.querySelector('.search_btn').addEventListener('click', function(e){
    e.preventDefault();
})
let x = document.querySelectorAll('.qr_image .title')
function search(){
    let input = document.querySelector('.search').value
    input = input.toLowerCase();
    if(input !== ''){
        for (let i = 0; i < x.length; i++) {
            if(!x[i].innerHTML.toLowerCase().includes(input)){
                x[i].closest('.saved_data').style.display = 'none'
            } else{
                x[i].closest('.saved_data').style.display = 'flex'
            }
        }
    }
}
document.getElementById('all').addEventListener('click', function(e){
    document.querySelector('.search').value = ' ';
    x.forEach(function(div){
        div.closest('.saved_data').style.display = 'flex'
    })
})