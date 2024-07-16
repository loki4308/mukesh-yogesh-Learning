const arr = [5, 1, 3, 2, 6];

// not proper method
function findsum(arr) {
    let sum = 0;
    for (let i = 0; i< arr.length; i++) {
        sum = sum = arr[i];
    }
    return sum;
}
console.log(findsum(arr));

const output = arr.reduce(function (acc, curr) {
    acc = acc = curr;
    return acc;
})