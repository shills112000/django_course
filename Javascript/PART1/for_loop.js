// for - loops through a number of times

// all the statements do the same
//num = num + 1
//num += 1
//num++

//for (statement1;statement2){
    //execute code
//}

// example
//for (var i = 0 ;i < 5; i++){
    // execute code
//}

for (var i =0; i < 5;i++){
    console.log ("Number is "+i);
}


// for/in - loops through a JS object

var word = "ABCDEFGHIJK"

for ( var i=0; i < word.length; i=i+2){

    console.log (word[i]);
}

// for/of - used with arrays