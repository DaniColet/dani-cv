// Visitor Counter Logic
const API_ENDPOINT = 'https://f0na88kvck.execute-api.us-east-1.amazonaws.com/prod/counter'; // e.g. https://xyz.execute-api.us-east-1.amazonaws.com/prod/counter

document.addEventListener('DOMContentLoaded', () => {
    const counterElement = document.getElementById('visitor-count');
    if (!counterElement) return;

    fetch(API_ENDPOINT)
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.json();
        })
        .then(data => {
            counterElement.textContent = data.count;
            // animateCounter(counterElement, 0, data.count, 1000); // Optional animation
        })
        .catch(error => {
            console.error('Error fetching visitor count:', error);
            counterElement.textContent = '-';
        });
});
