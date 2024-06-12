function isPalindrome(num) {
    // Convert the number to a string
    let numStr = num.toString();
    // Use JavaScript's built-in reverse() method to reverse the string
    let reversedStr = numStr.split('').reverse().join('');
    // Compare the original string to the reversed string
    return numStr === reversedStr;
  }
  console.log(isPalindrome(12321)); // true
  console.log(isPalindrome(12345)); // false
  console.log(isPalindrome(1001)); // true
    