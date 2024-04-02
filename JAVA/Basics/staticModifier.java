/*
 * the static keyword is used to create variables and methods
 *  that belong to the class itself rather than to instances of the class. 
 * When a member (variable or method) is declared as static,
 * it means there will be only one instance of that member shared across all instances of the class
 */

public class staticModifier {
    public static void main(String[] args){
        Friend friend1 = new Friend("vaibhav");
        Friend friend2 = new Friend("Shudanshu");
        Friend friend3 = new Friend("mahendra");
        Friend friend4 = new Friend("uttakarsh");

        System.out.println(Friend.numberOfFriends);

    }
    
}

class Friend{
    String name;
    static int numberOfFriends;
    Friend(String name){
        this.name = name;
        numberOfFriends++;   //here the number of friends will increse whenever new instance is created 
                            //therefore it won't create a copy of vairiable for each instance
                            // instead one copy will be shared as discribed above
    }
}
