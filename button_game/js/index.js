let colorsArr = ['blue', 'red', 'yellow','chartreuse','white','orange']
let game = document.getElementById('game');
let color = document.getElementById('color')
let stop = document.getElementById('stop')
let result = document.getElementById('result')
interval = setInterval(changeColor, 200);
let i = 0

let index = Math.floor(Math.random() * (6 - 1)) + 1;
color.innerHTML = colorsArr[index]
color.style.color = colorsArr[index]


function stopGame(){
    clearInterval(interval);
    if(color.innerHTML == game.style.background){
        result.innerHTML = 'You Win!!!'
        result.style.color = 'rgb(13, 34, 92)'
    }
    else{
        result.innerHTML = 'You Lose...'
        result.style.color= 'red'
    }
}

function changeColor(){
    if(i > 5)
        i = 0
    else
        i+=1
    // let index = Math.floor(Math.random() * (6 - 1)) + 1;
    game.style.background = colorsArr[i]
    
}
