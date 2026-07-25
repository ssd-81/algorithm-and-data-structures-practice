class Solution {
    public boolean isPalindrome(String s) {
        String cleanString = s.replaceAll("[^a-zA-Z0-9]","").toLowerCase();
        String reversedString = new StringBuilder(cleanString).reverse().toString();

        return cleanString.equals(reversedString);
    }
}
