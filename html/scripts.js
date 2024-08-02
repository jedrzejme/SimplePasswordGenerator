// Simple Password Generator
// Author: Jędrzej Bakalarski
// Github: https://github.com/jedrzejme/SimplePasswordGenerator

document.getElementById('generate').addEventListener('click', generatePassword);
document.getElementById('copy').addEventListener('click', copyToClipboard);

function generatePassword() {
    const length = document.getElementById('length').value;
    const uppercase = document.getElementById('uppercase').checked;
    const lowercase = document.getElementById('lowercase').checked;
    const digits = document.getElementById('digits').checked;
    const special = document.getElementById('special').checked;

    const upperChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowerChars = 'abcdefghijklmnopqrstuvwxyz';
    const digitChars = '0123456789';
    const specialChars = '!@#$%^&*()_+[]{}|;:,.<>?';

    let allChars = '';
    if (uppercase) allChars += upperChars;
    if (lowercase) allChars += lowerChars;
    if (digits) allChars += digitChars;
    if (special) allChars += specialChars;

    if (!allChars) {
        alert('You must select at least one character type!');
        return;
    }

    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * allChars.length);
        password += allChars[randomIndex];
    }

    document.getElementById('password').value = password;
}

function copyToClipboard() {
    const password = document.getElementById('password').value;
    if (!password) {
        alert('No password to copy!');
        return;
    }

    const tempInput = document.createElement('input');
    tempInput.value = password;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    alert('Password copied to clipboard!');
}
