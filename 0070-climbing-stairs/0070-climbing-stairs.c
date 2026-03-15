int solve(int n,int dp[]) {
    if(n==0||n==1)
        return 1;
    if(dp[n]!=-1)
        return dp[n];
    dp[n] = solve(n-1,dp)+solve(n-2,dp);
    return dp[n];
    
}
int climbStairs(int n){
    int dp[50];
    for(int i=0;i<50;i++)
        dp[i] = -1;
    
    return solve(n,dp);

}