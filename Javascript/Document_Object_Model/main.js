var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var headThree = document.querySelector('#three')

console.log("connected")

headOne.addEventListener("mouseover",function(){
    headOne.textContent = "Mouse currently over"
    headOne.style.color = "red"
})

headOne.addEventListener("mouseout",function(){
    headOne.textContent = "Mouse not over"
    headOne.style.color = "Blue"
})

headTwo.addEventListener("click",function(){
    headTwo.textContent = "clicked on"
    headTwo.style.color = "Green"
})

headThree.addEventListener("dblclick",function(){
    headThree.textContent = "double clicked on"
    headThree.style.color = "Green"
})