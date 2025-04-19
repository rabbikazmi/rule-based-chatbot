function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatBox = document.getElementById('chatBox');
    const userMessage = userInput.value;

    if (userMessage.trim() === '') return;

    // Display user message
    chatBox.innerHTML += `<div class="message user-message">${userMessage}</div>`;
    
    // Send the message to the Flask backend
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        const botResponse = data.response;
        
        // Display bot response with typing effect
        setTimeout(() => {
            chatBox.innerHTML += `<div class="message bot-message">${botResponse}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        }, 500);
    });

    // Clear input and scroll to bottom
    userInput.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Enter key functionality
document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Initial greeting
window.onload = function() {
    setTimeout(() => {
        document.getElementById('chatBox').innerHTML = 
            '<div class="message bot-message">👋 Welcome! I\'m here to help you learn about vaccines. Feel free to ask any questions about vaccine safety, schedules, side effects, or specific vaccines!</div>';
    }, 500);
}
