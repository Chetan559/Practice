import java.util.Scanner;
public class methods {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        methods logic = new methods();   // declaration of new object sub
        int a = 10;
        int b = 4;
        int c = add(a,b);  // call of static method
        int d = logic.sub(a,b);  // call of non-static method 
        System.out.println("For a :"+a+" and b :"+b);
        System.out.println("addition is : "+c);
        System.out.println("Subtraction is: "+d);
        int a1 = 5;
        int b1 = 14;
        int c1 = add(a1,b1);
        int d1 = logic.sub(a1,b1);
        System.out.println("For a :"+a1+" and b :"+b1);
        System.out.println(c1);
        System.out.println(d1);
        System.out.println("Enter a : ");
        int a2 = sc.nextInt();
        System.out.println("Enter b : ");
        int b2 = sc.nextInt();
        int c2 = add(a2,b2);
        int d2 = logic.sub(a2,b2);
        System.out.println("For a :"+a2+" and b :"+b2);
        System.out.println(c2);
        System.out.println(d2);
        sc.close();

    }
    int sub(int x, int y){  // here we didn't use static method instead we have associated method with object logic
        int z;
        if(x>y){
            z = x-y;
        }
        else{
            z = y-x;
        }
        return z;        
    }
    static int add( int x, int y){  //here we have used static method which associates the method with class itself
        int z;
        if(x>y){
            z = x+y;
        }
        else{
            z = (x+y)*10;
        }
        return z;        
    }
}
