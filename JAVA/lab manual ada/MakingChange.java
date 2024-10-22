import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class MakingChange {
// Method to solve the "Making Change" problem
public static int makeAChange(int[] denominations, int amount) {
int n = denominations.length;
// Create the matrix C with (n+1) rows and (amount+1) columns
int[][] C = new int[n + 1][amount + 1];
// Initialize the first column to 0 (no coins needed for amount 0)
for (int i = 0; i <= n; i++) {
C[i][0] = 0;
}
// Initialize the first row (except for the first element) to a large value (infinity)
for (int j = 1; j <= amount; j++) {
C[0][j] = Integer.MAX_VALUE - 1; // Using MAX_VALUE - 1 to avoid overflow
}
// Fill the matrix using the dynamic programming approach
for (int i = 1; i <= n; i++) {
for (int j = 1; j <= amount; j++) {
if (j < denominations[i - 1]) {
// If the denomination is greater than the amount
C[i][j] = C[i - 1][j];
} else {
// Choose the minimum between not using the current denomination or using it
C[i][j] = Math.min(C[i - 1][j], 1 + C[i][j - denominations[i - 1]]);
}
}
}
// If the value in C[n][amount] is still infinity, change is not possible
if (C[n][amount] == Integer.MAX_VALUE - 1) {
return -1; // Indicating that change is not possible
}
// Backtrack to find the coins used
List<Integer> coinsUsed = new ArrayList<>();
int i = n, j = amount;
while (i > 0 && j > 0) {
if (C[i][j] == C[i - 1][j]) {
i--; // Move to the previous row (denomination not used)
} else {
coinsUsed.add(denominations[i - 1]);
j -= denominations[i - 1];
}
}
// Print the matrix C
System.out.println("Matrix C:");
for (int row = 0; row <= n; row++) {
System.out.println(Arrays.toString(C[row]));
}
// Print the coins used
System.out.println("Coins used: " + coinsUsed);
// Return the minimum number of coins required
return C[n][amount];
}
public static void main(String[] args) {
int[] denominations = {1, 3, 4}; // Example denominations
int amount = 12; // Example amount
int minCoins = makeAChange(denominations, amount);
if (minCoins != -1) {
System.out.println("Minimum number of coins required: " + minCoins);
} else {
System.out.println("Change is not possible with the given denominations.");
}
}
}