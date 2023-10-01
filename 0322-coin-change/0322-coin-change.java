class Solution {

    public int coinChange(int[] coins, int amount) {
        // Create a memoization table, initialized with -1 indicating unreached states
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, -1);  // All values are initialized to -1
        dp[0] = 0;  // Base case: 0 coins are needed to make change for 0

        // Loop through each amount from 1 to the target amount
        for (int i = 1; i <= amount; i++) {
            // For each coin value, see if it can be used to reach the current amount
            for (int coin : coins) {
                if (i - coin >= 0 && dp[i - coin] != -1) {
                    // If the current amount can be reached,
                    // update the minimum coins needed for the current amount
                    dp[i] = dp[i] == -1 ? dp[i - coin] + 1 : Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount];
    }
}
