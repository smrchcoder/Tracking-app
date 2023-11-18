document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        console.log('Email:', email);
        console.log('Password:', password);

        const data = {
            email: email,
            password: password
        };

        fetch('/checklogin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            console.log('Result:', result);

            if (result.success) {
                errorMessage.textContent = result.message;
                setTimeout(function() {
                    window.location.href = '/path';
                }, 100);
            } else {
                errorMessage.textContent = result.message;
            }
        })
        .catch(error => {
            errorMessage.textContent = 'An error occurred. Please try again later.';
            console.error('Error:', error);
        });
    });
});
