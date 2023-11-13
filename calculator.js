let display = document.getElementById('display');

function appendToDisplay(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

function deleteLast() {
    display.value = display.value.slice(0, -1);
}

function calculate() {
    try {
        display.value = eval(display.value);
    } catch (error) {
        display.value = 'Error';
    }
}

// Numeric keys
for (let i = 0; i <= 9; i++) {
    let button = document.createElement('button');
    button.textContent = i;
    button.onclick = function () {
        appendToDisplay(i);
    };
    document.querySelector('.keys').appendChild(button);
}

// Operation keys
const operations = ['+', '-', '*', '/'];

for (let operation of operations) {
    let button = document.createElement('button');
    button.textContent = operation;
    button.onclick = function () {
        appendToDisplay(operation);
    };
    document.querySelector('.keys').appendChild(button);
}

// Additional buttons
let delButton = document.createElement('button
