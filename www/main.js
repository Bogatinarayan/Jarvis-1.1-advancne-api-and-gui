$(document).ready(function () {

    eel.init(); // Initialize eel

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });

    let isListening = false; // Flag for listening
    let isSpeaking = false; // Flag for responding

    // Mic button click event
    $("#MicBtn").click(function () {
        if (isSpeaking) {
            // Stop current speaking process if the mic button is clicked
            eel.stopSpeaking(); // Python method to stop the assistant from speaking
            isSpeaking = false;
        }

        if (!isListening) {
            isListening = true; // Set the flag to true for listening
            eel.playAssistantSound(); // Play the assistant sound
            $("#Oval").attr("hidden", false); // Show #Oval

            // Trigger Python listening function
            eel.allCommands()().then(() => {
                isListening = false; // Reset the flag after listening ends
            });
        }
    });

    // Function to handle speaking (response phase)
    eel.expose(startSpeaking);
    function startSpeaking() {
        isSpeaking = true; // Set the flag to true for speaking
        $("#Oval").attr("hidden", true); // Hide #Oval
        // You can optionally show a different animation or element here
        // Automatically activate mic after response
        setTimeout(function() {
            $("#MicBtn").click(); // Trigger mic button click to start listening again
        }, 500); // Delay to ensure the response has been delivered
    }

    // Function to stop speaking (reset state)
    eel.expose(stopSpeaking);
    function stopSpeaking() {
        isSpeaking = false; // Reset speaking flag
        $("#Oval").attr("hidden", false); // Show #Oval
        // Optional: Reset any animations or elements you want after speaking ends
    }

    // Keyup event for special key combinations
    function doc_keyUp(e) {
        if (e.key === 'j' && e.metaKey) {
            $("#MicBtn").click(); // Simulate a mic button click on keypress
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // Function to handle sending a message
    function PlayAssistant(message) {
        if (message !== "") {
            $("#Oval").attr("hidden", false); // Show #Oval
            isSpeaking = true; // Set speaking flag
            eel.allCommands(message).then(() => {
                stopSpeaking(); // Reset state when response is complete
            });
            $("#chatbox").val(""); // Clear the chatbox
            ShowHideButton(""); // Reset buttons
        }
    }

    // Toggle mic and send button
    function ShowHideButton(message) {
        if (message.length === 0) {
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        } else {
            $("#MicBtn").attr("hidden", true);
            $("#SendBtn").attr("hidden", false);
        }
    }

    // Keyup event for chatbox
    $("#chatbox").keyup(function () {
        let message = $("#chatbox").val();
        ShowHideButton(message);
    });

    // Send button click event
    $("#SendBtn").click(function () {
        let message = $("#chatbox").val();
        PlayAssistant(message);
    });

    // Enter key event for chatbox
    $("#chatbox").keypress(function (e) {
        if (e.which === 13) {
            let message = $("#chatbox").val();
            PlayAssistant(message);
        }
    });
});
