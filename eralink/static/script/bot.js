document.addEventListener('DOMContentLoaded', function () {
    const chatInput = document.getElementById("chat-input");
    const sendButton = document.getElementById("send-btn");
    const chatContainer = document.querySelector(".chat-container");
    const themeButton = document.getElementById("theme-btn");
    const deleteButton = document.getElementById("delete-btn");

    let userText = null;

    const loadDataFromLocalstorage = () => {
        const themeColor = localStorage.getItem("themeColor");

        document.body.classList.toggle("light-mode", themeColor === "light_mode");
        themeButton.textContent = document.body.classList.contains("light-mode") ? "dark_mode" : "light_mode";

        const defaultText = `<div class="default-text">
        <h1>ERA Link Chat-Bot</h1>
        <p>Start a conversation and explore the power of AI.</p>
    </div>`;

        chatContainer.innerHTML = localStorage.getItem("all-chats") || defaultText;
        chatContainer.scrollTop = chatContainer.scrollHeight;
    };

    const createChatElement = (content, className) => {
        const chatDiv = document.createElement("div");
        chatDiv.classList.add("chat", className);
        chatDiv.innerHTML = content;
        return chatDiv;
    };

    const showTypingAnimation = () => {
        const html = `<div class="chat-content">
            <div class="chat-details">
                <img src="https://cdn.freebiesupply.com/logos/large/2x/era-4-logo-png-transparent.png" alt="chatbot-img">
                <div class="typing-animation">
                    <div class="typing-dot" style="--delay: 0.2s"></div>
                    <div class="typing-dot" style="--delay: 0.3s"></div>
                    <div class="typing-dot" style="--delay: 0.4s"></div>
                </div>
            </div>
            <span class="material-symbols-rounded">content_copy</span>
        </div>`;
    
        const incomingChatDiv = createChatElement(html, "incoming");
        chatContainer.appendChild(incomingChatDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    
        // Perform an AJAX request to get a response from the server
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'getResponse?userMessage=' + userText, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                const responseHtml = `<div class="chat-content">
                    <div class="chat-details">
                        <img src="https://cdn.freebiesupply.com/logos/large/2x/era-4-logo-png-transparent.png" alt="chatbot-img">
                        <div class="response-content">
                            <p>${xhr.responseText}</p>
                        </div>
                    </div>
                </div>`;
    
                const animationDiv = chatContainer.querySelector(".typing-animation:last-child").parentNode;
                animationDiv.outerHTML = responseHtml;
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }
        };
        xhr.send();
    };
    

    const handleOutgoingChat = () => {
        userText = chatInput.value.trim();
        if (!userText) return;

        chatInput.value = "";
        chatInput.style.height = initialInputHeight + "px";

        const html = `<div class="chat-content">
            <div class="chat-details">
                    <img src="https://d3i7vug90am37q.cloudfront.net/app/uploads/2021/10/25150728/You.jpg" alt="user-img">
                <p>${userText}</p>
            </div>
        </div>`;

        const defaultTextElement = chatContainer.querySelector(".default-text");
        if (defaultTextElement) {
            chatContainer.removeChild(defaultTextElement);
        }
        
        const outgoingChatDiv = createChatElement(html, "outgoing");
        chatContainer.appendChild(outgoingChatDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;

        setTimeout(showTypingAnimation, 300);
    };

    deleteButton.addEventListener('click', function () {
        if (confirm("Are you sure you want to delete all the chats?")) {
            localStorage.removeItem("all-chats");
            loadDataFromLocalstorage();
        }
    });

    themeButton.addEventListener('click', function () {
        document.body.classList.toggle("light-mode");
        localStorage.setItem("themeColor", themeButton.textContent);
        themeButton.textContent = document.body.classList.contains("light-mode") ? "dark_mode" : "light_mode";
    });

    const initialInputHeight = chatInput.scrollHeight;

    chatInput.addEventListener('input', function () {
        chatInput.style.height = initialInputHeight + "px";
        chatInput.style.height = chatInput.scrollHeight + "px";
    });

    chatInput.addEventListener('keydown', function (e) {
        if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
            e.preventDefault();
            handleOutgoingChat();
        }
    });

    loadDataFromLocalstorage();

    sendButton.addEventListener('click', function () {
        handleOutgoingChat();
    });
});
