

//restart  # is id   . is class
var restart = document.querySelector("#b")

// all squares  td is all elements called td
var squares = document.querySelectorAll('td')

// clear squares
function clearBoard(){
  for (var i = 0; i < squares.length; i++){
    squares[i].textContent = '';
  }
}

// check the square marker

restart.addEventListener('click',clearBoard)

function changeMarker(){
  if (this.textContent === ""){
    this.textContent = "X";
  }else if (this.textContent === "X"){
    this.textContent = "O";
  } else if (this.textContent === "O") {
    this.textContent = "";
  }
}

for (var i = 0; i < squares.length; i++){
  squares[i].addEventListener('click', changeMarker)
}
// for loop to add event listeners to all squares
