document.getElementById('shuttleForm').addEventListener('submit', function (event) {
    event.preventDefault();
  
    // Collect form data
    const shuttleIdElement = document.getElementById('shuttleId');
    const nameElement = document.getElementById('name');
    const routeIdElement = document.getElementById('routeId');
    console.log(shuttleIdElement);
    const shuttleId = shuttleIdElement.value;
    const name = nameElement.value;
    const routeId = routeIdElement.value;
    console.log(shuttleId);
    // Create JSON object
    const jsonData = {
      "shuttle_id": parseInt(shuttleId),
      "name": name,
      "route_id": parseInt(routeId)
    };
  
    // Make a POST request to the API
    fetch('/shuttel', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(jsonData),
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.text(); // Read the response as text
      })
      .then(data => {
        try {
          //const jsonData = JSON.parse(data);
          console.log('Success:', jsonData);
          // Handle success, e.g., show a success message to the user
          alert('Form submitted successfully!');
        } catch (jsonError) {
          console.error('Error parsing JSON:', jsonError);
          alert('Error parsing the server response. Please try again.');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        // Handle error, e.g., show an error message to the user
        alert('Error submitting the form. Please try again.');
      });
  });
  