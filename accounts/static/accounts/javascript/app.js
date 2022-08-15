const alert = document.querySelector('.alert');
const submitBtn = document.querySelector('.input_submit');
const emailValue = document.querySelector('#email').value;

// This is where the error meassage can be manipulated.

submitBtn.addEventListener('click', function(){
    
    // Condition to check if the email is found or not.
    if( emailValue === ' '){
        alert.classList.remove('hide')
    }
    setTimeout(function(){
        alert.classList.add('hide')
    }, 3000)
})
// document.querySelector('.alert_text button').addEventListener("click", function(){
//     alert.classList.add('hide')
// })
const btn = document.querySelector('.button')
if(btn){
    btn.addEventListener("click", function(){
        alert.classList.add('hide')
    })
}