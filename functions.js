// Function statement (or) Function declaration
function a() {
    console.log("A called");
}
a()

// Function expression
var b = function() {
    console.log("B called");
}
b()

// Anonymous function
// function() { 

// }

// Named function expression
var c = function xyz() {
    console.log("C called");
}
c()

//difference between parameters & arguments
function d(param1) {
    console.log(param1, "called");
}
d("D") 

//First class function
function e(param1) {
    console.log(param1);
}
e(function(){
    console.log("E called");
})

//or

function f() {
    return function(){
        console.log("F called")
    }
}
console.log(f())

//Arrow function 