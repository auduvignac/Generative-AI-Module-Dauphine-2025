async function askQuestion() {
    const question = document.getElementById("question").value;
    const response = await fetch("/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
    });
    const data = await response.json();
    document.getElementById("response").innerText = data.answer;
}
