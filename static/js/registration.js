// Function for toggling
const toggleForm = () => {
    const container = document.querySelector('.container');
    container.classList.toggle('active');
};


// Function to validate password
const validatePassword = () => {
    const password = document.getElementById('password').value;
    const confirm_password = document.getElementById('confirm_password').value;
    const passwordError = document.getElementById('passwordError');

    if (password !== confirm_password) {
      passwordError.style.display = 'block'; // Show error message
      return false; // Prevent form submission
    } else {
      passwordError.style.display = 'none'; // Hide error message
      return true; // Proceed with form submission
    }
};


// Function to check password instantly when user types in confirm password field
const checkPasswordInstantly = () => {
    const password = document.getElementById('password').value;
    const confirm_password = document.getElementById('confirm_password').value;
    const passwordError = document.getElementById('passwordError');

    if (password !== confirm_password) {
      passwordError.style.display = 'block'; // Show error message
    } else {
      passwordError.style.display = 'none'; // Hide error message
    }
};


// Add event listener to confirm password input field
document.getElementById('confirm_password').addEventListener('input', checkPasswordInstantly);


// Function to toggling the password visibility
const togglePasswordVisibility = (inputId) => {
    const passwordInput = document.getElementById(inputId);
    const eyeIcon = document.querySelector(`span.toggle-password[onclick="togglePasswordVisibility('${inputId}')"]`);

    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      eyeIcon.textContent = "👁️";
    } else {
      passwordInput.type = "password";
      eyeIcon.textContent = "🔒";
    }
};