import java.util.Arrays;
import java.util.Collections;
class MakingChangeGreedy {

    // Function to make change using greedy algorithm
    public static int[] makeChange(int[] denominations, int amount) {
        // Sort denominations in descending order
        Integer[] denoms = Arrays.stream(denominations).boxed().toArray(Integer[]::new);
        Arrays.sort(denoms, Collections.reverseOrder());

        int[] result = new int[denoms.length]; // To store number of coins for each denomination

        // Iterate over each denomination
        for (int i = 0; i < denoms.length; i++) {
            int coin = denoms[i];
            // While the amount is greater than or equal to the coin value
            while (amount >= coin) {
                amount -= coin; // Subtract the coin value from the amount
                result[i]++;    // Increment the count for this denomination
            }
        }
        // Return the result array which indicates the number of coins for each denomination
        return result;
    }

    // Main function to test the algorithm
    public static void main(String[] args) {
        int[] denominations = {1, 5, 10, 25}; // Example coin denominations
        int amount = 63; // Example amount for which we need to make change

        int[] change = makeChange(denominations, amount);
        System.out.println("Making change for " + amount + " using denominations:");

        // Output the results
        for (int i = 0; i < denominations.length; i++) {
            if (change[i] > 0) {
                System.out.println(denominations[i] + " : " + change[i] + " coins");
            }
        }
    }
}
