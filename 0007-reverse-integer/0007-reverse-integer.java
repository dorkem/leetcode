class Solution {
    public int reverse(int x) {
        boolean isNegat = x < 0;
        String str = new StringBuilder(Integer.toString(Math.abs(x))).reverse().toString();
        try {
            int result = Integer.parseInt(str);
            return isNegat ? -result : result;
        } catch (NumberFormatException e) {
            return 0;
        }
    }
}