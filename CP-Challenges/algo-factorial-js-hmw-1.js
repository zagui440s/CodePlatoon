function factorial(num){
    if(num === 0 || num === 1){return 1}
    let arr = []

    for(let i = 1; i <= num; i++){
        arr.push(i)
    }
    return arr.reduce((a,b) => a*b,1)
}


console.log(factorial(4)) // 24
console.log(factorial(0)); // 1, 1
console.log(factorial(1)); // 1, 1
console.log(factorial(2)); // 2 * 1, 2
console.log(factorial(3)); // 3 * 2 * 1, 6
console.log(factorial(5)); // 5 * 4 * 3 * 2 * 1, 120
