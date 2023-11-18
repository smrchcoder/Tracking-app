document.addEventListener('DOMContentLoaded', function() {
    const signupForm = document.getElementById('signup-form');
    const errorMessage = document.getElementById('error-message');

    signupForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const email = document.getElementById('email').value;
        const newUsername = document.getElementById('new-username').value;
        const newPassword = document.getElementById('new-password').value;
        const confirmPassword = document.getElementById('confirm-password').value;
        const phone = document.getElementById('phone').value;

        // Simple validation
        if (newPassword !== confirmPassword) {
            errorMessage.textContent = 'Passwords do not match.';
        } else {
            errorMessage.textContent = 'Sign-up successful! Redirecting to login page...';

            // Simulate a delay (e.g., 2 seconds) for the success message
            setTimeout(function() {
                // Redirect to the login page after a successful signup
                window.location.href = 'login.html';
            }, 2000);
        }
    });
});
