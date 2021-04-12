alert("Welcome to your test");

var Names=false;
var First_Name = prompt ("What is your firstname?:")

var Last_Name = prompt ("What is your last name?:")

var Age = prompt ("What is your Age:")
var Height = prompt ("What is your Height in cm?:")
var Pet_Name = prompt ("What is your Pets name?:")
x = Pet_Name.length;
alert (Pet_Name[x-1]);

if (First_Name[0] == Last_Name[0] && Age > 20 && Age < 30 && Height >= 170 && Pet_Name[x-1] == "y"){
    
    console.log("You are a spy")
}
