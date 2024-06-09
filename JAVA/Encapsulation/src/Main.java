public class Main {
    public static void main(String[] args) {
//        Encapsulation = the atribtes of the class will be hidden or private,
//                        Can only be accessed through the methods (setter/getter),
//                        you should make the attributes private if yuou don't intentd to make them public/protected

        Car car =new Car("Honda" ,"City",2008);
//        System.out.println(car.year);
//        this shows error bcoz these attributes are private and can only be accessed by the car class to get these values use getter methods
        System.out.print(car.getMake()+" ");
        System.out.print(car.getModel()+" ");
        System.out.print(car.getYear());
//        the getModel(),getMake(),getYear() are the getter methods
    }
}

