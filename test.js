const {performance} = require('perf_hooks');

//* Write a function that accepts an input n
//* the returns the sum from 1 up to n


//! Math approach
const addUpToMath = (n) => (n * (n + 1)) / 2

//! For loop approach
const addUpToSingleForLoop = (n) => {
    let total = 0;
    for(let i = 1; i <= n; i++){
        total += i;
    }
    return total;
}

//! Nested For loop approach
const addUpToNested = (n) => {
    let total = 0;
    for(let i = 1; i <= n; i++){
        for(let j = 1; j <= i; j++){
            total += 1;
        }
    }
    return total;
}


//! Timing function
//* algo 1 is the math approach
//* algo 2 is the for loop approach
//* algo 3 is the nested for loop approach
const checkTime = (n, algo) => {
    let t1 = performance.now();
    if(algo === 1){
        addUpToMath(n)
    }else if(algo === 2){
        addUpToSingleForLoop(n)
    }else{
        addUpToNested(n)
    }
    let t2 = performance.now();
    console.log(`Time elapsed: ${(t2 - t1) / 1000} seconds`)
}

console.log('check 100')
checkTime(100, 1);
checkTime(100, 2);
checkTime(100, 3);

console.log('check 1000')
checkTime(1000, 1);
checkTime(1000, 2);
checkTime(1000, 3);

console.log('check 10000')
checkTime(100000, 1);
checkTime(100000, 2);
checkTime(100000, 3);