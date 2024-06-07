package pakage2;
import pakage1.*;

public class Asub extends A {
    public static void main(String[] Args) {
        C c = new C();
        Asub asub = new Asub();
        System.out.println(c.defaultMessage);
//        becoz of defalut access modifier the defaultMessage can be accessed from different class form same pakage
        System.out.println(asub.protectedMessage);
    }
}
