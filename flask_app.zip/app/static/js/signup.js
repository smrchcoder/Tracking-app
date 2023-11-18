document.addEventListener('DOMContentLoaded', function() {
    const signupForm = document.getElementById('signup-form');
    const errorMessage = document.getElementById('error-message');

    signupForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const email = document.getElementById('email').value;
        const newUsername = document.getElementById('new-username').value;
        const newPassword = document.getElementById('new-password').value;

        // Prepare the data to be sent to the API
        const data = {
            email: email,
            name: newUsername,
            password: newPassword
        };

        // Make an HTTP POST request to the API
        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                errorMessage.textContent = result.message;
                // Simulate a delay (e.g., 2 seconds) for the success message
                setTimeout(function() {
                    // Redirect to the login page after a successful signup
                    window.location.href = '/login';
                }, 200);
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