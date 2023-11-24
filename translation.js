function translateText() {
    const text = document.getElementById('text').value;
    const targetLanguage = document.getElementById('targetLanguage').value;

    fetch('http://127.0.0.1:5000/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, target_language: targetLanguage }),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('translationResult').textContent = data.translation;
        })
        .catch(error => console.error('Error:', error));
}
