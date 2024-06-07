package pakage1;
import pakage2.*;

public class A {
    protected String protectedMessage ="This is protected Access modifier" ;
    public static void main(String[] Args){
        C c =new C();
//        System.out.println(c.defaultMessage);
//        as the defaultMessagfe is Default access modifier it cannot be accessed from pakage 1
        System.out.println(c.publicMessage);
    }
}
