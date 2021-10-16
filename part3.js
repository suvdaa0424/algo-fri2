//1. Live Code Solution 1:
//Given an array of random srings, Write a function that will return a new array 
//with only the words that contain the letter e.

randomStrings = ['elephant', 'cat', 'pEnguin', 'bird', 'dog', 'rat', 'lion', 'parrot']

function onlyFindE(array) {
    const onlyE_Array = [];
    const everythingElse = [];
    for (let index = 0; index < array.length; index++) {
        const string= array[index];
        if (string.toLowerCase().includes('e')) {
            onlyE_Array.push(string)
        } else {
            everythingElse.push(string)
        }  
    }
    return onlyE_Array;
}

console.log(onlyFindE(randomStrings))


//2. Live Code Solution 2:
// Given an array of random strings. Write a function that will return a new array
//with only the words that are 4 letters or more.

function fourOrMore(array) {
    const newArray = [];
    const oldArray = [];
    for (let index = 0; index < array.length; index++) {
        const string = array[index];
        if (string.length >= 4) {
            newArray.push(string)
        }
        else {
            oldArray.push(string)

        }
    }
    return newArray;
}
console.log(fourOrMore(randomStrings))


// Independent Code Solution 1:

// Write a function that takes two arguments, String1 and String2. Join these strings together
// and reverse the newString.

function Add_and_Reverse(String1, String2) {
    const addString = String1.concat(" ", String2);
    console.log(addString)
    const revString = addString.split('').reverse().join('')
    console.log(revString)
}
Add_and_Reverse('hello', 'you')



//Independent Code Solution 2:
//Write a function that, given a string, will always return the 4th charachter. And if
//the string is too short, the console will print "too short of a string".

function find4thChar(input) {
    var string = input;

    if (string.length < 4) {
        console.log("too short of a string")
    } else {
        var position = string.charAt(3);
        console.log(position)
    }
    
}
find4thChar('hello')
find4thChar('hey')
find4thChar('hi')