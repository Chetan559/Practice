class MyExceptionMain {

    static int currentBal = 5000;
    
    public static void main(String args[]) {
    
    try {
    
    int amount = Integer.parseInt(args[0]);
    
    withdraw(amount);
    
    } catch (Exception ex) {
    
    System.out.println("Caught");
    
    System.out.println(ex.getMessage());
    
    }
    
    }
    
    public static void withdraw(int amount) throws Exception
    
    {
    
    int newBalance = currentBal - amount;
    
    if(newBalance<1000) {
    
    throw new MyException("Darshan Exception");
    
    }
    
    }
    
    }

class MyException extends Exception
{

public MyException(String s)

{

// Call constructor of parent (Exception)

super(s);

}

}