// Stand in Line(queue)
function nextInLine(arr, item) {
    // Only change code below this line
    arr.push(item);
    const items = arr.shift();
    return items;
    // Only change code above this line
  }
  
  // Setup
  let testArr = [1, 2, 3, 4, 5];
  
  // Display code
  console.log("Before: " + JSON.stringify(testArr));
  console.log(nextInLine(testArr, 6));
  console.log("After: " + JSON.stringify(testArr));
//   Understanding Boolean Values
function welcomeToBooleans() {
    // Only change code below this line
  
    return true; // Change this line
//  here we changed the return value from false to true 
    // Only change code above this line
  }
//   Use Conditional Logic with If Statements
function trueOrFalse(wasThatTrue) {
    // Only change code below this line
    if(wasThatTrue == true){
      return "Yes, that was true";
    }
    return "No, that was false";
  
  
    // Only change code above this line
  
  }

  // Comparisons with the Logical Or Operator
  function testLogicalOr(val) {
    // Only change code below this line
  
    if (val<10 || val >20) {
      return "Outside";
    }
    // Only change code above this line
    return "Inside";
  }
  
  testLogicalOr(15);
  // Introducing Else Statements
  
  function testElse(val) {
    let result = "";
    // Only change code below this line
  
    if (val > 5) {
      result = "Bigger than 5";
    }else {
      result = "5 or Smaller";
    }
  
    // Only change code above this line
    return result;
  }
  
  testElse(4);
  // Introducing Else If Statements
  function testElseIf(val) {
    if (val > 10) {
      return "Greater than 10";
    } else if (val < 5) {
      return "Smaller than 5";
    } else{
  
     return "Between 5 and 10";
  }}
  
  testElseIf(7) 
  // Logical Order in If Else Statements
  function orderMyLogic(val) {
    if (val < 5) {
      return "Less than 5";
    }else if (val < 10) {
      return "Less than 10";
    } else {
      return "Greater than or equal to 10";
    }
  }
  
  orderMyLogic(7);
  // Chaining If Else Statements
  function testSize(num) {
    // Only change code below this line
   if (num < 5){ return "Tiny";}
   else if (num < 10){ return "Small";}
   else if (num < 15){ return "Medium";}
   else if (num < 20){ return "Large";}
   else { return "Huge"}
  
    // Only change code above this line
  }
  
  testSize(7);
  // Golf Code
  const names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"];

function golfScore(par, strokes) {
  // Only change code below this line
  if (strokes == 1){return "Hole-in-one!";}
  else if (strokes <= par-2){return "Eagle";}
  else if (strokes <= par-1){return "Birdie";}
  else if (strokes <= par){return "Par";}
  else if (strokes <= par+1){return "Bogey";}
  else if (strokes <= par+2){return "Double Bogey";}
  else if (strokes >= par+3){return "Go Home!";}
  // Only change code above this line
}

golfScore(5, 4);
// Selecting from Many Options with Switch Statements
function caseInSwitch(val) {
  let answer = "";
  // Only change code below this line
switch (val){
  case 1:
   answer = "alpha";
   break;
  case 2:
   answer = "beta";
   break;
  case 3:
   answer = "gamma";
   break;
  case 4:
   answer = "delta";
   break;
}


  // Only change code above this line
  return answer;
}

caseInSwitch(1);
// Adding a Default Option in Switch Statements
  /*n a switch statement you may not be able to specify all possible values as case statements. Instead, you can add the default statement which will be executed if no matching case statements are found. Think of it like the final else statement in an if/else chain.*/
  function switchOfStuff(val) {
    let answer = "";
    // Only change code below this line
     switch(val) {
       case "a" :
        return "apple";
        break;
       case "b" :
        return "bird";
        break;
       case "c" :
        return "cat";
        break;
       default:
        return "stuff";
        break;
  
     }
  
  
    // Only change code above this line
    return answer;
  }
  
  switchOfStuff(1);
  // Multiple Identical Options in Switch Statements
  function sequentialSizes(val) {
    let answer = "";
    // Only change code below this line
    switch (val){
      case 1:
      case 2:
      case 3:
        return "Low";
        break;
      case 4:
      case 5:
      case 6:
        return "Mid";
        break;
      case 7:
      case 8:
      case 9:
        return "High";
        break;
    }
  
  
    // Only change code above this line
    return answer;
  }
  
  sequentialSizes(1);
  // Replacing If Else Chains with Switch 
  function chainToSwitch(val) {
    let answer = "";
    // Only change code below this line
     switch (val){
       case "bob":
      answer = "Marley";
      break;
       case 42:
      answer = "The Answer";
      break;
       case 1: 
      answer = "There is no #1";
      break;
       case 99:
      answer = "Missed me by this much!";
      break;
       case 7:
      answer = "Ate Nine";
      break;
      } 
    // if (val === "bob") {
    //   answer = "Marley";
    // } else if (val === 42) {
    //   answer = "The Answer";
    // } else if (val === 1) {
    //   answer = "There is no #1";
    // } else if (val === 99) {
    //   answer = "Missed me by this much!";
    // } else if (val === 7) {
    //   answer = "Ate Nine";
    // }
  
    // Only change code above this line
    return answer;
  }
  
  chainToSwitch(7);
  // Returning Boolean Values from Functions
  function isLess(a, b) {
    // Only change code below this line
    // if (a < b) {
    //   return true;
    // } else {
    //   return false;
    // }
    return a<b;
    // Only change code above this line
  }
  
  isLess(10, 15);
  // Return Early Pattern for Functions
  // Setup
function abTest(a, b) {
  // Only change code below this line
    if( a< 0 || b<0){
      return undefined ;
    }


  // Only change code above this line

  return Math.round(Math.pow(Math.sqrt(a) + Math.sqrt(b), 2));
}

abTest(2,2);
// Counting Cards 
let count = 0;

function cc(card) {
  // Only change code below this line
  switch (card){
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
     count++;
      break;
    case 7:
    case 8:
    case 9:
      count = count;
      break;
    case 10:
    case "J":
    case "Q":
    case "K":
    case "A":
      count--;
      break
    
  }
  let answer = "";
   if(count > 0){
     answer ="Bet";
   }else {
     answer = "Hold"
   } 
   return count +" "+ answer;
  // Only change code above this line
}

cc(2); cc(3); cc(7); cc('K'); cc('A');
// Build JavaScript Objects
const myDog = {
  // Only change code below this line
  "name": "tommy",
  "legs": 3,
  "tails":1,
  "friends":["jack","jeal"]

  // Only change code above this line
};

// Accessing Object Properties with Dot Notation
// Setup
const testObj = {
  "hat": "ballcap",
  "shirt": "jersey",
  "shoes": "cleats"
};

// Only change code below this line
const hatValue = testObj.hat;      // Change this line
const shirtValue = testObj.shirt;    // Change this line

// Accessing Object Properties with Bracket Notation
// Setup
const testObj1 = {
  "an entree": "hamburger",
  "my side": "veggies",
  "the drink": "water"
};

// Only change code below this line
const entreeValue = testObj1["an entree"];   // Change this line
const drinkValue = testObj1["the drink"];    // Change this line

// Accessing Object Properties with Variables

// Setup
const testObj2 = {
  12: "Namath",
  16: "Montana",
  19: "Unitas"
};

// Only change code below this line
const playerNumber = 16;  // Change this line
const player = testObj2[playerNumber];   // Change this line

// Updating Object Properties

// Setup
const myDog1 = {
  "name": "Coder",
  "legs": 4,
  "tails": 1,
  "friends": ["freeCodeCamp Campers"]
};

// Only change code below this line
myDog1.name ="Happy Coder" ;

// Add New Properties to a JavaScript Object

const myDog2 = {
  "name": "Happy Coder",
  "legs": 4,
  "tails": 1,
  "friends": ["freeCodeCamp Campers"]
};

myDog2.bark="woof";

// Delete Properties from a JavaScript Object
