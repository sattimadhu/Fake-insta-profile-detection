let subBtn=document.querySelector('#submit');
let clear=document.querySelector('.clear');
let form=document.querySelector('.box');
subBtn.addEventListener('click',function(event){
event.preventDefault();
form.submit();
})
clear.addEventListener('click',function(event){
    event.preventDefault()
    form.reset();
})
