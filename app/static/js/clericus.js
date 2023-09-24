
// JavaScript for `clericus.html` page
// File path: `app/static/js/clericus.js`
// Updated: 09-24-2023

$(document).ready(function () {
    $("#send-msg").click(function () {
        var userQuery = document.getElementById("user_query").value;
        var chatMessages = document.getElementById("chat-messages");
        document.getElementById("user_query").value = "";

        // Update to handle newlines in user messages
        var formattedUserQuery = userQuery.replace(/\n/g, "<br>");
        chatMessages.innerHTML += "<div class='message-wrapper user-message'><p>" + formattedUserQuery + "</p></div>";

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
                // Update to handle newlines in Clericus responses
                var formattedResponse = data.response.replace(/\n/g, "<br>");
                chatMessages.innerHTML += "<div class='message-wrapper clericus-message'><p>" + formattedResponse + "</p></div>";
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
