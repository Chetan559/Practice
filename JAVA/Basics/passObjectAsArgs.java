public class passObjectAsArgs {
    public static void main(String[] args){
        Garage garage = new Garage();
        Car car1 = new Car("Honda City");
        Car car2 = new Car("Tavera");
        Car car3 = new Car("Innova");
        garage.parked(car1);
        garage.parked(car2);
        garage.parked(car3);

    }
}
class Garage{
    void parked(Car car){
        System.out.println("Your "+ car.name + " is parked");
    }
}

class Car{
    String name;
    Car(String name){
        this.name =name;
    }
}