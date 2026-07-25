class Solution {
    private boolean isAlphanumeric(char c){
        return (c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
    }

    private char toLowerCase(char c){
        if (c >= 'A' && c <= 'Z'){
            return (char)(c + 32); // 'a'-'A' = 32
        }
        return c;
    }

    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;

        while(l < r){
            while(!isAlphanumeric(s.charAt(l)) && l < r){
                l ++;;
            }

            while(!isAlphanumeric(s.charAt(r)) && l < r){
                r --;
            }

            if(toLowerCase(s.charAt(l)) != toLowerCase(s.charAt(r))){
                return false; 
            }
            l++; r--;
        }
        return true;
    }
}
