// script.js

// Function to add text to a div
function addTextToDiv() {
    var myDiv = document.getElementById('myDiv');
    myDiv.textContent = 'Hello, this text was added by JavaScript!';
}

// Run the function to add text when the page loads
window.onload = addTextToDiv;
