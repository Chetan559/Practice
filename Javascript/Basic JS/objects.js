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

  // Setup
const myDog3 = {
    "name": "Happy Coder",
    "legs": 4,
    "tails": 1,
    "friends": ["freeCodeCamp Campers"],
    "bark": "woof"
  };
  
  // Only change code below this line
  delete myDog3.tails;

//   Using Objects for Lookups

// Setup
function phoneticLookup(val) {
    let result = "";
     
    // Only change code below this line
    /*switch(val) {
      case "alpha":
        result = "Adams";
        break;
      case "bravo":
        result = "Boston";
        break;
      case "charlie":
        result = "Chicago";
        break;
      case "delta":
        result = "Denver";
        break;
      case "echo":
        result = "Easy";
        break;
      case "foxtrot":
        result = "Frank";
    }
    */
    const lookup = {
      "alpha":"Adams",
      "bravo":"Boston",
      "charlie":"Chicago",
      "delta":"Denver",
      "echo":"Easy",
      "foxtrot": "Frank"
    }
     result = lookup[val];
    // Only change code above this line
    return result;
  }
  
  phoneticLookup("charlie");
//   here we converted the switch to object

// Testing Objects for Properties

/*To check if a property on a given object exists or not, you can use the .hasOwnProperty() method. someObject.hasOwnProperty(someProperty) returns true or false depending on if the property is found on the object or not.*/ 

function checkObj(obj, checkProp) {
    // Only change code below this line
      let check1 = obj.hasOwnProperty(checkProp);
       if (check1 == true){
         return obj[checkProp];
       } else {
         return "Not Found";
       }
    // Only change code above this line
  }

//   Manipulating Complex Objects
/*Sometimes you may want to store data in a flexible Data Structure. A JavaScript object is one way to handle flexible data. They allow for arbitrary combinations of strings, numbers, booleans, arrays, functions, and objects. */
const myMusic = [
    {
      "artist": "Billy Joel",
      "title": "Piano Man",
      "release_year": 1973,
      "formats": [
        "CD",
        "8T",
        "LP"
      ],
      "gold": true
    },//we have added the below lines
    {
      "artist": "arjit singh",
      "title": "pal pal",
      "release_year": 2018,
      "formats": [
        "CD",
        "8T",
        "LP"
      ],
      "gold": true
    }
  ];

//   Accessing Nested Objects
/*The sub-properties of objects can be accessed by chaining together the dot or bracket notation.*/
const myStorage = {
    "car": {
      "inside": {
        "glove box": "maps",
        "passenger seat": "crumbs"
       },
      "outside": {
        "trunk": "jack"
      }
    }
  };
//  this is how we acces the data in nested objects 
  const gloveBoxContents = myStorage.car.inside["glove box"];

//   Accessing Nested Arrays
/*As we have seen in earlier examples, objects can contain both nested objects and nested arrays. Similar to accessing nested objects, array bracket notation can be chained to access nested arrays. */

const myPlants = [
    {
      type: "flowers",
      list: [
        "rose",
        "tulip",
        "dandelion"
      ]
    },
    {
      type: "trees",
      list: [
        "fir",
        "pine",
        "birch"
      ]
    }
  ];
//    this is how we acces the data in nested arrays 
  const secondTree = myPlants[1].list[1];
