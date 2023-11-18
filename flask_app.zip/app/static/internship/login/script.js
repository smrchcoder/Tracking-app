document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Simple validation
        if (username === 'user' && password === 'password') {
            // Successful login, you can redirect to another page here
            errorMessage.textContent = 'Login successful!';
        } else {
            errorMessage.textContent = 'Invalid username or password';
        }
    });
});
