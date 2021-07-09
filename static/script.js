// *** for navbar mobile screen 
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
        x.className += " fixedElement";
    } else {
        x.className = "topnav";
    }
}
// *** end  for navbar mobile screen 

// *** for botton to top

//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

// *** end for botton to top








// พับไว้ก่อน
// *** navbar new

// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
// window.onscroll = function() { scrollFunction() };

// function scrollFunction() {
//     if (document.body.scrollTop > 1 || document.documentElement.scrollTop > 1) {
//         document.getElementById("myTopnav").style.padding = "30px 10px";
//         document.getElementById("logo").style.fontSize = "15px";
//     } else {
//         document.getElementById("myTopnav").style.padding = "50px 7px";
//         document.getElementById("logo").style.fontSize = "30px";
//     }
// }

// *** end navbar new