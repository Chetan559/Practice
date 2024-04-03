public class inheritance {
    public static void main(String[] args){
    Car car = new Car();
    Byke bike = new Byke();

    car.Go();
    bike.Stop();
    System.out.println(car.doors);
    System.out.println(bike.padels);
    }
}

class Vehical{ // here vehical is super class
    double topSpeed = 100;
    String name;
     
    void Go(){
        System.out.println("your Vehical is Going");
    }
    void Stop(){
        System.out.println("your Vehical is Stoped");
    }
}

class Car extends Vehical{ // subclass of vehical
    int doors =4;
    int wheels = 4;
}

class Byke extends Vehical{  // subclass of 
    int wheels =2;
    int padels =2;
}
