public class Main {
    public static void main(String[] args) {

        Car car1 =new Car("Honda" ,"City",2008);
        Car car2 = new Car("Suzuki","Swift",2010);

        System.out.println(car1);
        System.out.println(car2);
        System.out.print(car1.getMake()+" ");
        System.out.print(car1.getModel()+" ");
        System.out.print(car1.getYear());
        System.out.println();
        System.out.print(car2.getMake()+" ");
        System.out.print(car2.getModel()+" ");
        System.out.print(car2.getYear());
//        car2 = car1;
        car2.copy(car1);
//        the copy function will copy all the value stored at address of car1 to the address of car2 .hence the addess of car2 won't change
        System.out.println();
        System.out.println(car1);
        System.out.println(car2);
        System.out.print(car2.getMake()+" ");
        System.out.print(car2.getModel()+" ");
        System.out.print(car2.getYear());
    }
}

