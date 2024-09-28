const display = document.getElementById('display');

function appendToDisplay(input){
    display.value += input;
}

function clearDisplay(){
    display.value = '';
}

function calculate(){
    try{
        display.value = eval(display.value);
    }
    // if it catches an error from eval() function i.e. 7+ = return error
    catch(error){
        display.value = 'error';
    }
    
}