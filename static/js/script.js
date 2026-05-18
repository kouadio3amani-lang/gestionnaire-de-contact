const container = document.querySelector('.container');
const registerBtn = document.querySelector('.register-btn');
const loginBtn = document.querySelector('.login-btn');
registerBtn.addEventListener('click',()=>{
    container.classList.add('active');
})
loginBtn.addEventListener('click',()=>{
    container.classList.remove('active');
})
setTimeout(function () {
    let alerts = document.querySelectorAll('.alert, .alert-correct, .alert-error, .alert-success, .alert-warning');

    alerts.forEach(function(alert) {
        alert.style.transition = "0.4s";
        alert.style.opacity = "0";

        setTimeout(() => {
            alert.remove();
        }, 500); 
    });

}, 5000); 

