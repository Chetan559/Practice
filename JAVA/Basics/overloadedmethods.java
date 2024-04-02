public class overloadedmethods {
    public static void main(String[] args){
     int a=1;
     int b=2;
     int c=3;
     int d=4;
     double a1 = 10.7;
     double b1 = 5.7;
     double c1 = 2.7;
     double d1 = 1.9;
     int x = add(a, b);
     System.out.println(x);
     int y= add(a, b,c);
     System.out.println(y);
     int z = add(a, b, c, d);
     System.out.println(z);
     double x1 = add(a1, b1);
     System.out.println(x1);
     double y1= add(a1, b1, c1);
     System.out.println(y1);
     double z1 = add(a1, b1, c1, d1);
     System.out.println(z1);
     

    }
    static int add(int x, int y){
        System.out.println("Overloaded method #1 called");
        return x+y;
    }
    static int add(int x, int y, int z){
        System.out.println("Overloaded method #2 called");
        return x+y+z;
    }
    static int add(int w, int x, int y, int z){
        System.out.println("Overloaded method #3 called");
       return w+x+y+z;
    }
    static double add(double x, double y){
        System.out.println("Overloaded method #4 called");
        return x/y;
    }
    static double add(double x, double y, double z){
        System.out.println("Overloaded method #5 called");
        return x/y/z;
    }
    static double add(double w, double x, double y, double z){
        System.out.println("Overloaded method #6 called");
       return w/x/y/z;
    }
}
