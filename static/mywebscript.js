window.RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    fetch("/emotionDetector", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: textToAnalyze })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("system_response").innerHTML = data.formatted_response;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("system_response").innerHTML = "Error occurred while analyzing the text.";
    });
}
