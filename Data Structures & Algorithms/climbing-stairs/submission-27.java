class Solution {
    public int climbStairs(int n) {
        int[] arr = new int[n];

        arr[n-1] = 1;
        arr[n-2] = 1;

        for(int i = n-3; i >= 0; i--){
            arr[i] = arr[i+1] + arr[i+2];
        }

        return arr[0] + arr[1];
    }
}
