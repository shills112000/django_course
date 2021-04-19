// Let's type this into the console, follow along with the video lecture

var p = document.querySelectorAll('p')

// Show Text
console.log(p)

p.textContent = "new text";

// Reassign Text
//x.textContent = "new"

// Refresh the page
// Show actual HTML
//x.innerHTML

// Edit HTML
//x.innerHTML = "This is <strong>BOLD</strong>"

// Can't do that with just textContent

/////////////////
// Attributes //
///////////////

//var special = document.querySelector("#special")
//var specialA = y.querySelector("a")

//specialA.getAttribute("href")

//specialA.setAttribute("href","https://www.amazon.com")


var special = document.querySelector("#special")
undefined
special
<h4 id=​"special">​"I am another "<em>​header​</em>​" with the special id.
      "<a href=​"https:​/​/​www.facebook.com">​FACEBOOK LINK​</a>​</h4>​
var specialA = special.querySelector("a")
undefined
specialA
<a href=​"https:​/​/​www.facebook.com">​FACEBOOK LINK​</a>​
specialA.getAttribute("href")
"https://www.facebook.com"
specialA.setAttribute("href", "https://amazon.com")
undefined
