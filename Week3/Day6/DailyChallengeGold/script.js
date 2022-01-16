const numbers = [5,0,9,1,7,4,2,6,3,8];

// numbers.toString();
// numbers.join("|");

// for (let i = 0; i < numbers.length; i++) { //loops through the array integers
//     for(let n = 0; n < numbers.length; n++) { //loop through the array integers for comparison purposes
//         if(numbers[i] < numbers[i + 1]) {
//             numbers.swap(numbers[i + 1], numbers[i]);
//             console.log(numbers)
//         }
//     }
// }


for(let i = 0; i < numbers.length - 1; i++) {
    for(let j = 0; i < numbers.length - 1 - i; j++) {
        if(numbers[j] > numbers[j + 1]) {
            let temp = numbers[j];
            numbers[j] = numbers[j + 1];
            numbers[j + 1] = temp;
        }
    }
    
console.log(numbers)
}
