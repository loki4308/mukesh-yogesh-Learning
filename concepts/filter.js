const arr = [5,1,3,2,6];

// filter odd number
function isOdd(x) {
    return x % 2;
}

// filter even number
function isEven(x) {
    return x % 2 === 0;
}

// greter then 4
function greater(x) {
    return x > 4;
}

const output = arr.filter(greater);

// OR

const output2 = arr.filter((x) => x > 4); // easy way

console.log(output);
console.log(output2)