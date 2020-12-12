class Solution {
    public int concatenatedBinary(int n) {
        int mod = 1000000007;
        int ans = 0;
        int pow = 1;
        for (int i=n; i >=1; i--){
            int bin = i;
            while (bin > 0) {
                if ((bin & 1) == 1){
                    ans = (ans + pow) %mod;
                }
                bin = bin >> 1;
                pow = (pow *2) % mod;
            }
        }
        return ans;
    }
}