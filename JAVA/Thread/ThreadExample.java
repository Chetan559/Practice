import java.lang.*;
// Step 1: Create a class that extends Thread
class MyThread extends Thread {
    // Step 2: Override the run method to define the task
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(Thread.currentThread().getName() + " - Count: " + i);
            try {
                // Make the thread sleep for a bit to simulate some work
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class ThreadExample {
    public static void main(String[] args) {
        // Step 3: Create an instance of MyThread
        MyThread thread1 = new MyThread();
        MyThread thread2 = new MyThread();

        // Step 4: Call the start method to begin execution
        thread1.start();
        thread2.start();

        // Main thread prints its own messages
        for (int i = 1; i <= 5; i++) {
            System.out.println(Thread.currentThread().getName() + " - Main Count: " + i);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
