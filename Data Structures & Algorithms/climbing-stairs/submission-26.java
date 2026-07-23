class Solution {
    public int climbStairs(int n) {
        int last, secondLast, temp;
        last = 1;
        secondLast = 1;

        for(int i = n-2; i >= 0; i--){
            temp = last;
            secondLast = last + secondLast;
            last = temp;
        }

        return secondLast;
    }
}
