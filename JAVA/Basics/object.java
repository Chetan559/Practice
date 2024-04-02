/*
 * object = it is a instance of class that may contain attributes and methods
 * think of Attributes as features/Characterstics of object
 * think of Method as the functions that object can perform
*/

public class object {
    public static void main(String[] args){
        Car myCar1 = new Car();
        Car myCar2 = new Car();
        System.out.println(myCar1.model);
        System.out.println(myCar1.year);
        System.out.println();
        System.out.println(myCar2.model);  // here both car1 and car2 will have same characteristics to have unique value we use constructor
        System.out.println(myCar2.year);
         
        myCar1.breaks();
        myCar2.clucth();
        
    }
}


class Car{
    String model ="Honda City";
    int year = 2008;
    String colour ="Golden";
    double price = 1000000.00;

    void breaks (){
        System.out.println("You applied breaks");
    }

    void clucth(){
        System.out.println("You applied Clutch");
    }


}