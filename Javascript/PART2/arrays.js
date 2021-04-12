var country1= "USA"
var country2= "England"
var country3= "China"

var countries = ["USA","China","England"]

console.log("test" + countries[0]) // first elemet


// immutalbe (cannot change)
// mutability (can be changed)

countries[0] = "France"

console.log("test" + countries[0]) // first elemet

var mixedDataType= [true,20,"string"]
console.log(mixedDataType.length)

// add remove elemets
var myArray = ['one','two','three']

var lastItem = myArray.pop()
console.log(lastItem)

// push item

myArray.push("four")
console.log(myArray[2])

// show last item in array
console.log("Last item in array: "+ myArray[myArray.length -1])

// nest arrays

var matrix = [[1,2,3],[4,5,6],[7,8,9]]

// array itteration

var arr = ['A','B','C']

for (letter of arr){
    console.log(letter);
}

//for  (letter of arr){
//    alert(letter);
//}

arr.forEach(alert) // same as above for

function addAwesome(name){
    console.log(name + " is awesome!");
}

addAwesome("Django")

var topics = ["python","django","science"]

topics.forEach(addAwesome)