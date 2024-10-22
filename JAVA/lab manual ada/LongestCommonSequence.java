class LongestCommonSubsequence {
    // Function to find the length of LCS and also print the LCS
    public static String findLCS(String X, String Y) {
    int m = X.length();
    int n = Y.length();
    // Step 1: Create the DP table
    int[][] T = new int[m + 1][n + 1];
    // Step 2: Fill the DP table
    for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
    if (X.charAt(i - 1) == Y.charAt(j - 1)) {
    T[i][j] = T[i - 1][j - 1] + 1; // Case 1: characters match
    } else {
    T[i][j] = Math.max(T[i - 1][j], T[i][j - 1]); // Case 2: no match
    }
    }
    }
    // Step 3: Backtrack to find the LCS
    int i = m, j = n;
    StringBuilder lcs = new StringBuilder();
    while (i > 0 && j > 0) {
    if (X.charAt(i - 1) == Y.charAt(j - 1)) {
    lcs.append(X.charAt(i - 1)); // Add to LCS if characters match
    i--;
    j--;
    } else if (T[i - 1][j] > T[i][j - 1]) {
    i--; // Move up
    } else {
    j--; // Move left
    }
    }
    // Since we append characters in reverse, reverse the string
    return lcs.reverse().toString();
    }
    public static void main(String[] args) {
    // Example input
    String X = "BDCB";
    String Y = "BACDB";
    // Step 4: Call the function and print the result
    String lcs = findLCS(X, Y);
    System.out.println("Longest Common Subsequence: " + lcs);
    System.out.println("Length of LCS: " + lcs.length());
    }
    }