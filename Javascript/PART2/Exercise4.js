
var studentNames=[];

function addStudent(){
    newStudent = prompt ("Enter the Name of the student:");
    studentNames.push (newStudent)
}

function remove(){
    var remName = prompt ("Enter the Name of the student:");
    index = studentNames.indexOf(remName);  // get the index of the name
    studentNames.splice(index,1); // remove element in array
}

function display(){
    console.log (studentNames)
}

var command = "false"

while (command !== "quit"){
    command = prompt ("Enter the command you want:");

    if (command === "add"){
        addStudent();
    }
    if (command === "remove"){
        remove();
    }
    if (command === "display"){
        display();
    }
}
