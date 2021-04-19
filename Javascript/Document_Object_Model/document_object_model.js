
// important attributes

// document.URL
// document.body
// document.head
// document.links

// many methods for grabbing specific elements from the DOM:

// document.getElementById()
// document.getElementByClassName()
// document.getElementByTagName()
// document.querySelector()
// document.querySelectorAll()

console.log("test" + document.URL); // file location
console.log(document.body) // body of document
console.log(document.head) // head of document
console.log(document.links) // links in document

console.log(document.getElementById('pickme'))

console.log(document.getElementsByClassName('myul'))

console.log(document.getElementsByTagName('h1'))

// queryselector is like grabbing elements but uses the css style selector

console.log(document.querySelector("#pickme"))

console.log(document.querySelectorAll(".myul"))

//change object properties

var myheader = document.querySelector("h1")
console.log (myheader)
myheader.style.color = 'green' // change the header to red




