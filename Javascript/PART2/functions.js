// Functions

//function name (parameter1,parameter2){
    //code to execute
//}
helloYou("Simon")  // execute the function
function helloYou(name){
    console.log("hello "+name);
}


addNum(2,3);
function addNum(num1,num2){
    console.log(num1+num2)
}

// set default parmeters
helloSomeone()
function helloSomeone(name="trevor"){
    console.log("hello "+ name)
}

// return results
var output = formal()
console.log ("Welcome " + output)
function formal(name="Sam",title="Sir"){
    return name + " " + title
}

function timesFive(NumInput){
    var result = NumInput * 5
    return result
}

for (var i =1; i < 13;i++ ){
    output=timesFive(i)
    console.log(output)
}

// Global Scope

var v =  " GLOBAL V"

var stuff = "GLOBAL STUFF"

function fun(stuff){
    console.log(v);
    stuff = "Reassign stuff in fun"
    console.log(stuff)
}
fun()
console.log(stuff)
