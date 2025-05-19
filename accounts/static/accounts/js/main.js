const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add('active');
});

loginBtn.addEventListener('click', () => {
    container.classList.remove('active');
});

document.addEventListener('DOMContentLoaded', function () {
    const loginMessageBox = document.getElementById('login-error-box');
    const signupMessageBox = document.getElementById('signup-error-box');

    const loginInputs = document.querySelectorAll('.sign_in input');
    loginInputs.forEach(input => {
        input.addEventListener('focus', () => {
            if (loginMessageBox) {
                loginMessageBox.style.display = 'none';
            }
        });
    });

    const signupInputs = document.querySelectorAll('.sign_up input');
    signupInputs.forEach(input => {
        input.addEventListener('focus', () => {
            if (signupMessageBox) {
                signupMessageBox.style.display = 'none';
            }
        });
    });
});
