// Objects - same as python dictionaires

// key value pair

// {key1 : "value 1". key2 : 'value2}


var car = {Make:"ford",year:1999,model:"fiesta"};

console.log (car["model"])

var myNewObject = {a:"hello",b:[1,2,3],c:{inside:["a","b"]}}

console.log(myNewObject['a']) // will be "hello"
console.log(myNewObject['b'][1]) // will be 2
console.log(myNewObject['c']['inside'][1]) // will be "b"

// changing values

car ['model'] = "robin"
console.log (car["model"])

car ['year'] +=1;  // add a year
console.log (car["year"])

console.dir(car)  // show the whole obkect in the console

// show all keys and items of object 
for (key in car){
    console.log(key);
    console.log (car[key])
}

//object methods , can have function methods of an object

var car = {
    make: "toyota",
    year: "1999",
    model: "Camry",
    carAlert: function(){
        alert("We have a car here!")
    }
}

// special key word  - this -

var myObj = {
    prop: 37,
    reportProp: function(){
        return this.prop;
    }
}

console.log(myObj.reportProp()); // logs 37

// add methods (function) to a object

var simple = {
    prop : "Hello",
    myMethod : function(){
        console.log("The myMethod was called");
    }
}

console.dir(simple)
simple.myMethod()

var myObj = {
    name: "Jose",
    greet: function (){
        console.log ("Hello " + this.name)
    }
}

console.log(myObj['name'])
myObj.greet();
