public class overloadedVolume {
    public static void main(String[] args){
        shape cube = new shape();
        shape RectangularCube = new shape();
        shape Sphere = new shape();

        cube.Volume(5.8);
        RectangularCube.Volume(5.9,12.0);
        Sphere.Volume(7);
    }
}

class shape{
    double length;
    double breath;
    double width;
    void Volume(int radius){
        this.length = radius;
        this.breath = radius;
        this.width = radius;
        System.out.println("Volume of Spere : "+(4/3)*3.14*length*breath*width);
    }
    void Volume(double length, double width){
        this.length = length;
        this.breath = length;
        this.width = width;
        System.out.println("Volume of Rectangle cube : "+length*breath*width);
    }

    void Volume(double length){
        this.length = length;
        this.breath = length;
        this.width = length;
        System.out.println("Volume of Cube :"+length*breath*width);
    }
}
