// JavaScript for `clericus.html` page
// Updated: 09-21-2023

$(document).ready(function () {
    $("#send-msg").click(function () {
        var userQuery = document.getElementById("user_query").value;
        var chatMessages = document.getElementById("chat-messages");
        document.getElementById("user_query").value = "";

        var userMsgDiv = document.createElement("div");
        userMsgDiv.className = "user-message";
        userMsgDiv.innerHTML = "User: " + userQuery;
        chatMessages.appendChild(userMsgDiv);

        var thinkingElement = document.createElement("div");
        thinkingElement.className = "bot-message thinking";
        thinkingElement.innerHTML = "Clericus: Thinking...";
        chatMessages.appendChild(thinkingElement);

        fetch("/clericus", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: userQuery, session_id: session_id }),
        })
            .then((response) => response.json())
            .then((data) => {
                var botMessageElement = document.createElement("div");
                botMessageElement.className = "bot-message";
                botMessageElement.innerHTML = "Clericus: " + data.response;
                chatMessages.replaceChild(botMessageElement, thinkingElement);
            })
            .catch((error) => {
                var errorMsg = document.createElement("div");
                errorMsg.className = "error-message";
                errorMsg.innerHTML = "Clericus: An error occurred. Please try again.";
                chatMessages.appendChild(errorMsg);
            });
    });

    $(document).keypress(function (e) {
        if (e.which == 13) {
            $("#send-msg").click();
        }
    });

    const session_id =
        new Date().toISOString() + "-" + Math.random().toString(36).substr(2, 9);
});
