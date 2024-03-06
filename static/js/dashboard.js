document.getElementById("startChattingBtn").addEventListener("click", function() {
    // Call a function to generate room ID and password
    generateRoomIdAndPassword();
  });

function generateRoomIdAndPassword() {
    // Generate room ID and password
    const { roomId, password } = generateRoomDetails();
    
    // Copy room ID and password to clipboard
    copyToClipboard([roomId, password], ["Room ID", "Password"]);
    
    // Show alert to inform the user
    alert("Room ID and password copied to clipboard!");
}

function generateRoomDetails() {
    // Generate room ID and password logic goes here
    const roomId = generateRoomId();
    const password = generatePassword();
    return { roomId, password };
}

function generateRoomId() {
    // Generate unique room ID logic goes here
    return Math.random().toString(36).substr(2, 8).toUpperCase(); // Example: "ABC12345"
}

function generatePassword() {
    // Generate password logic goes here
    return Math.random().toString(36).substr(2, 10); // Example: "Abc123xyz"
}

function copyToClipboard(text, label) {
    // Create a text area to hold the text
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed"; // Ensure it's not displayed on the screen
    document.body.appendChild(textArea);
    
    // Select and copy the text to the clipboard
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
    
    // Log message to console
    console.log(`${label} copied: ${text}`);
}