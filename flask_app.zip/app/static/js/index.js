document.addEventListener('DOMContentLoaded', function() {
    const coordinateForm = document.getElementById('coordinate-form');
    const intermediateCoordinatesContainer = document.getElementById('intermediate-coordinates-container');
    const addCoordinateButton = document.getElementById('add-coordinate');
    const errorMessage = document.getElementById('error-message');

    let coordinateCounter = 0;

    addCoordinateButton.addEventListener('click', function() {
        const intermediateCoordinateDiv = document.createElement('div');
        intermediateCoordinateDiv.classList.add('form-group');

        const intermediateCoordinateInput = document.createElement('input');
        intermediateCoordinateInput.type = 'text';
        intermediateCoordinateInput.name = `intermediate-coordinate-${coordinateCounter}`;
        intermediateCoordinateInput.placeholder = 'Intermediate Coordinate';
        intermediateCoordinateInput.required = true;

        const removeCoordinateButton = document.createElement('button');
        removeCoordinateButton.type = 'button';
        removeCoordinateButton.textContent = 'Remove';

        removeCoordinateButton.addEventListener('click', function() {
            intermediateCoordinatesContainer.removeChild(intermediateCoordinateDiv);
        });

        intermediateCoordinateDiv.appendChild(intermediateCoordinateInput);
        intermediateCoordinateDiv.appendChild(removeCoordinateButton);

        intermediateCoordinatesContainer.appendChild(intermediateCoordinateDiv);

        coordinateCounter++;
    });

    coordinateForm.addEventListener('submit', async function(event) {
        event.preventDefault();

        const allCoordinates = [];
        const deviceId = document.getElementById('route-id').value; // Update to route-id
        const routeName = document.getElementById('route-name').value; // New field
        const initialLat = document.getElementById('initial-lat').value;
        const initialLng = document.getElementById('initial-lng').value;
        const destinationLat = document.getElementById('destination-lat').value;
        const destinationLng = document.getElementById('destination-lng').value;

        const intermediateCoordinateDivs = document.querySelectorAll('.form-group input[name^="intermediate-coordinate-"]');
        intermediateCoordinateDivs.forEach(function(input) {
            const intermediateCoordinate = input.value;
            allCoordinates.push(intermediateCoordinate);
        });

        const data = {
            device_id: deviceId,
            name: routeName, // New field
            ilat: initialLat,
            ilng: initialLng,
            dlat: destinationLat,
            dlng: destinationLng,
            intermidate_cord: allCoordinates
        };

        try {
            const response = await fetch('/coordinate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                const result = await response.json();
                if (result.success) {
                    errorMessage.textContent = result.message;

                    coordinateForm.reset();
                    alert(result.message);
                } else {
                    errorMessage.textContent = result.message;
                    coordinateForm.reset();
                    alert(result.message);
                }
                
            } else {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
        } catch (error) {
            errorMessage.textContent = 'An error occurred. Please try again later.';
            console.error('Error:', error);
        }
    });
});
