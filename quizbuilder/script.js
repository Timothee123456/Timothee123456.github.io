const validateBtn = document.getElementById('validateBtn');
const resetBtn = document.getElementById('resetBtn');
const textboxElements = document.querySelectorAll('.textbox');

// Validate answers
validateBtn.addEventListener('click', () => {
    textboxElements.forEach((textbox) => {
        const userAnswer = textbox.value.trim().toLowerCase();
        const correctAnswer = textbox.getAttribute('answer').trim().toLowerCase();
        
        // Remove previous validation classes
        textbox.classList.remove('correct', 'incorrect', 'empty');
        
        // Add validation class
        if (userAnswer === correctAnswer) {
            textbox.classList.add('correct');
        } else if (userAnswer !== '') {
            textbox.classList.add('incorrect');
        } else {
            // Empty answer - show correct answer in red
            textbox.classList.add('empty');
            textbox.value = textbox.getAttribute('answer');
            textbox.readOnly = true;
        }
    });
});

// Reset answers
resetBtn.addEventListener('click', () => {
    textboxElements.forEach(textbox => {
        textbox.value = '';
        textbox.classList.remove('correct', 'incorrect', 'empty');
        textbox.readOnly = false;
    });
});

console.log('Test loaded successfully!');
