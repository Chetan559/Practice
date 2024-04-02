/*
 * constructor = a special method that is called when an object is iniciated  
 */

 public class constructor {
    public static void main(String[] args){
        Human human1 = new Human("chetan",19,172);
        Human human2 = new Human("Sudhanshu",19,175);
        Human human3 = new Human("mahendra",19,160);
        System.out.println("name of #1 human is "+ human1.getName() + ", age is " + human1.getAge()+" and height is "+ human1.getHeight());
        System.out.println("name of #2 human is "+ human2.getName() + ", age is " + human2.getAge()+" and height is "+ human2.getHeight());
        System.out.println("name of #3 human is "+ human3.getName() + ", age is " + human3.getAge()+" and height is "+ human3.getHeight());
        human3.setHeight(169.50);
        System.out.println("name of #3 human is "+ human3.getName() + ", age is " + human3.getAge()+" and height is "+ human3.getHeight());
    }
}

class Human{
    private String name;    // here we have used private "acess modifier"
    private int age;
    private double height;

    Human(String name, int age, double height){   // this is a constructor here with 3 parameters as input
        this.name = name;     // "this" keyword is used here to differntiate between local and instance variable
        this.age = age;       // here "this" helps to set the value of instance vaiable equal to local variable
        this.height = height;
    }
     
    public String getName(){  // this is a getter here {returns the value[accesor]}
        return name;
    }

    public int getAge(){
        return age;
    }

    public double getHeight(){
        return height;
    }

    public void setHeight(double height){   // this is a setter here {sets or updates the value [mutator]}
        this.height = height;
    }

}

/*
 *       OUTPUT
 name of #1 human is chetan, age is 19 and height is 172.0
 name of #2 human is Sudhanshu, age is 19 and height is 175.0
 name of #3 human is mahendra, age is 19 and height is 160.0
 name of #3 human is mahendra, age is 19 and height is 169.5
 */