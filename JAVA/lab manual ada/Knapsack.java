import java.util.ArrayList;
import java.util.List;

class Knapsack {

    // Function to implement TRACE_KNAPSACK and retrieve selected items
    public static void traceKnapsack(int[] w, int[] v, int M, int[][] V) {
        int n = w.length;
        List<Integer> SW = new ArrayList<>(); // To store selected weights 
        List<Integer> SP = new ArrayList<>(); // To store selected profits

        int i = n; // Indexing starts from the last item 
        int j = M; // Maximum capacity of the knapsack

        while (j > 0 && i > 0) {
            // Check if the current item is included in the optimal solution 
            if (V[i][j] == V[i - 1][j]) {
                i--; // Move to the previous item
            } else {
                // Include the current item
                SW.add(w[i - 1]); // Add weight to selected items 
                SP.add(v[i - 1]); // Add value to selected items
                j -= w[i - 1]; // Reduce remaining capacity 
                i--; // Move to the previous item
            }
        }

        // Output the selected items and total value 
        System.out.println("Selected Weights: " + SW);
        System.out.println("Selected Values: " + SP);
    }

    // Function to solve the knapsack problem using dynamic programming 
    public static int[][] knapsackDP(int[] w, int[] v, int M) {
        int n = w.length;
        int[][] V = new int[n + 1][M + 1];

        // Build the table in bottom-up manner 
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= M; j++) {
                if (w[i - 1] <= j) {
                    // Include the item if it fits
                    V[i][j] = Math.max(V[i - 1][j], v[i - 1] + V[i - 1][j - w[i - 1]]);
                } else {
                    // Exclude the item 
                    V[i][j] = V[i - 1][j];
                }
            }
        }

        // Return the DP table 
        return V;
    }

    public static void main(String[] args) {
        // Weights and values of items 
        int[] weights = {2, 3, 4, 5};
        int[] values = {3, 4, 5, 6};
        int capacity = 8; // Knapsack capacity

        // Solve the knapsack problem
        int[][] V = knapsackDP(weights, values, capacity);

        // Traceback to find selected items 
        traceKnapsack(weights, values, capacity, V);

        // Print the maximum value that can be obtained 
        System.out.println("Maximum Value: " + V[weights.length][capacity]);
    }
}
