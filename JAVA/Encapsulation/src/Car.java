public class Car {
    private String make;
    private String model;
    private int year;
    Car(String make,String model,int year){
        this.model=model;
        this.make=make;
        this.year=year;
    }
    public String getMake(){
        return make;
    }
    public String getModel(){
        return model;
    }
    public int getYear(){
        return year;
    }

}
