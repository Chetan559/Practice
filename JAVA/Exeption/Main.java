import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class Main {
    public static void main(String[] args) {
        // Check if the user has provided a mathematical expression
        if (args.length == 0) {
            System.out.println("Please provide a mathematical expression as a command-line argument.");
            return;
        }

        // Combine all command-line arguments into a single string
        StringBuilder expression = new StringBuilder();
        for (String arg : args) {
            expression.append(arg).append(" ");
        }

        // Evaluate the mathematical expression
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");

        try {
            Object result = engine.eval(expression.toString().trim());
            System.out.println("Result: " + result);
        } catch (ScriptException e) {
            System.out.println("Invalid mathematical expression: " + e.getMessage());
        }
    }
}
