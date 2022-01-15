let form = document.getElementById("form");
let heading = document.getElementById('heading');
let text = document.getElementById('text')

function display(){
    heading.innerHTML = "Hello, " + text.value;
}