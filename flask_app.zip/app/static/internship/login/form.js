document.addEventListener('DOMContentLoaded', function() {
    const coordinateForm = document.getElementById('coordinate-form');
    const intermediateCoordinatesContainer = document.getElementById('intermediate-coordinates-container');
    const addCoordinateButton = document.getElementById('add-coordinate');

    addCoordinateButton.addEventListener('click', function() {
        const input = document.createElement('input');
        input.type = 'text';
        input.name = 'intermediate-coordinate';
        input.required = true;

        intermediateCoordinatesContainer.appendChild(input);
    });

    coordinateForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // Retrieve and process the coordinates (initial, destination, intermediates)
        const initialCoordinate = document.getElementById('initial-coordinate').value;
        const destinationCoordinate = document.getElementById('destination-coordinate').value;
        const intermediateCoordinates = [...document.getElementsByName('intermediate-coordinate')].map(input => input.value);

        // Example: Display the coordinates in the console
        console.log('Initial Coordinate:', initialCoordinate);
        console.log('Destination Coordinate:', destinationCoordinate);
        console.log('Intermediate Coordinates:', intermediateCoordinates);
    });
});
