document.addEventListener('DOMContentLoaded', function () {
    let timerSeconds;  // Declare timerSeconds globally

    const requestCodeButton = document.getElementById('sendCode');
    const sendconfirmationCodeButton = document.getElementById('sendconfirmationCode');
    const resendCodeButton = document.getElementById('resendCode');
    const sendCodeTimer = document.getElementById('sendCodeTimer');
    const phoneNumberInput = document.querySelector('#numberDialog input[type="number"]');
    const codeInput = document.querySelector('#codeDialog input[type="number"]');
    
    let globalPhoneNumber;

    const displayedPhoneNumberElement = document.querySelector("#displayedPhoneNumber");

    // Event listener for the send code button
    requestCodeButton.addEventListener('click', function () {
        const phoneNumber = phoneNumberInput.value;
        globalPhoneNumber = phoneNumber;
    
        // Fetch request to send verification code
        fetch('/accounts/send_verification_code/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ phone_number: phoneNumber }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response from send_verification_code:', data);
            // Handle the response, update UI, etc.
        })
        .catch(error => {
            console.error('Error in send_verification_code:', error);
            // Handle errors
        });
    
        // Start the timer when the code is sent
        timerSeconds = 120; // Reset the timer to its initial value
        updateTimerDisplay();
        startTimer();
        displayedPhoneNumberElement.innerHTML = phoneNumber;
    });
    
    // Event listener for the login button
    sendconfirmationCodeButton.addEventListener('click', function () {
        const confirmation_code = document.querySelector("input[name=confirmation_code]").value;
    
        // Fetch request to login with confirmation code
        fetch('/accounts/login_with_confirmation_code/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ confirmation_code: confirmation_code, phone_number: globalPhoneNumber }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response from login_with_confirmation_code:', data);
            window.location.href = '/';
            // Handle the response, update UI, etc.
        })
        .catch(error => {
            console.error('Error in login_with_confirmation_code:', error);
            // Handle errors
        });
    
        // Start the timer when the code is sent
        // timerSeconds = 120; // Reset the timer to its initial value
        // updateTimerDisplay();
        // startTimer();
    });
    
    // Event listener for the resend code button
    resendCodeButton.addEventListener('click', function () {
        console.log('Resend code button clicked!');

        // Your logic to resend the verification code goes here

        // Start the timer when the code is resent
        timerSeconds = 120; // Reset the timer to its initial value
        updateTimerDisplay();
        startTimer();
    });

    // ... (existing code)

    // Initial setup of the timer display
    updateTimerDisplay();

    // Function to update the timer display
    function updateTimerDisplay() {
        const minutes = Math.floor(timerSeconds / 60);
        const seconds = timerSeconds % 60;
        sendCodeTimer.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    }

    // Function to start the timer
    function startTimer() {
        requestCodeButton.disabled = true; // Disable the send button during the countdown
        resendCodeButton.disabled = true; // Disable the resend button during the countdown

        const timerInterval = setInterval(function () {
            timerSeconds--;

            if (timerSeconds <= 0) {
                clearInterval(timerInterval);
                requestCodeButton.disabled = false; // Enable the send button when the timer reaches zero
                resendCodeButton.disabled = false; // Enable the resend button when the timer reaches zero
            }

            updateTimerDisplay();
        }, 1000);
    }

    // Function to retrieve CSRF token from cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Additional event listeners
    document.getElementById('editPhoneNumber').addEventListener('click', function () {
        var displayedPhoneNumber = document.getElementById('displayedPhoneNumber').textContent;
        document.getElementById('phoneNumberInput').value = displayedPhoneNumber;
    });
});


var btn_close = document.querySelector(".btn-close");
btn_close.addEventListener('click', function () {
    btn_close.parentElement.style.display = 'none';
});