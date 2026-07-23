class Solution {
    public int climbStairs(int n) {
        if(n == 1){
            return 1;
        }
        if(n == 2){
            return 2;
        }
        int[] arr = new int[n+1];

        arr[n-1] = 1;
        arr[n] = 1;

        for(int i = n-2; i >= 0; i--){
            arr[i] = arr[i+1] + arr[i+2];
        }

        return arr[0];
    }
}
