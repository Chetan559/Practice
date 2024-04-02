public class arrayOfObjects {
    public static void main(String[] args){
        Food food1 = new Food("pizza");
        Food food2 = new Food("Sabji");
        Food food3 = new Food("pasta");

        //Food[] refrigirator = {food1,food2,food3};
        
        // another way of using array
        
        Food[] refrigirator = new Food[3];
        refrigirator[0] = food1;
        refrigirator[1] = food2;
        refrigirator[2] = food3;
        
        
        for(int i =0; i<3 ;i++){
            System.out.println(refrigirator[i].name);
        }
    }
}

class Food{
    String name;
    Food(String name){
        this.name = name;
    }    
}