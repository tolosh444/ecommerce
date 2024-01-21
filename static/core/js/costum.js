// Get the radio button elements
const sizeRadios = document.querySelectorAll('input[name="size"]');
const colorRadios = document.querySelectorAll('input[name="color"]');

// Add event listeners to the radio buttons
sizeRadios.forEach((radio) => {
  radio.addEventListener('change', handleSizeSelection);
});

colorRadios.forEach((radio) => {
  radio.addEventListener('change', handleColorSelection);
});

// Event handler for size selection
function handleSizeSelection(event) {
  const selectedSize = event.target.value;
  // Perform actions based on the selected size
  console.log('Selected size:', selectedSize);
}

// Event handler for color selection
function handleColorSelection(event) {
  const selectedColor = event.target.value;
  // Perform actions based on the selected color
  console.log('Selected color:', selectedColor);
}
