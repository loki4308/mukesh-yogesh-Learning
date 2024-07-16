// iteration method
function factorial(num) {
    let array = [];                 // [1,2,3,4,5]

    for (var i = 1; i <= num; i++) {
        array.push(i);                // inseting the number one by one
    }
    
    let answer = array.reduce(function(a,b) {   //reduce the array value in single number
        return a*b;
    })
    return answer;
}

console.log(factorial(5));

// recursion method

function facto(num) {
    if (num == 1){
        return 1;
    }
    else {
        return num * facto(num-1);
    }
}

console.log(facto(5));