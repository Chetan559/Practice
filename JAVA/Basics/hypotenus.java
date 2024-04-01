import java.util.Scanner;

class hypotenus{
    public static void main(String[] args){
            Scanner sc = new Scanner(System.in);

            double a;
            double b;
            double c;

            System.out.println("Enter Side 1:");
            a = sc.nextDouble();
            System.out.println("Enter Side 2:");
            b = sc.nextDouble();
            
            c = Math.sqrt((a*a)+(b*b));
            System.out.println("the hypotenus for sides "+ a + " and "+b+" is "+c);

    }
}