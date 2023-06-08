document.getElementById('check-form').addEventListener('submit', function (event) {
    // Prevents the form from being submitted in the default way, 
    // which would cause a page reload.
    event.preventDefault();

    // Get the values from the form elements.
    const keysInput = document.getElementById('keys-input');
    const textInput = document.getElementById('text-input');
    const dateMinInput = document.getElementById('min-date');
    const dateMaxInput = document.getElementById('max-date');

    const keys = keysInput.value;
    const text = textInput.value;
    const dateMin = dateMinInput.value;
    const dateMax = dateMaxInput.value;

    // If the text is empty, we don't need to do anything.
    if (!text) {
        return;
    }

    // We send a POST request to the server.
    fetch('https://test1029.herokuapp.com/check', {
    // fetch('http://127.0.0.1:8000/check', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        // We send the form data in JSON format.
        body: JSON.stringify({
            text: text,
            keys_to_retrieve: keys,
            date_min: dateMin,
            date_max: dateMax,
        }),
    })
    .then(response => response.json())
    .then(data => {
        let output = '';
        output += 'Result: <br>' + data.result;

        // Add the html images to the output
        output += data.image;

        // Set the innerHTML of 'result' to the output
        document.getElementById('result').innerHTML = output;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
