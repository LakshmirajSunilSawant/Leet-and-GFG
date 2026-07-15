class Solution {
    public int[] rearrangeArray(int[] nums) {
        int l = nums.length;
        int p = 0;
        int n = 0;
        int pos[] = new int[l/2];
        int neg[] = new int[l/2];

        for (int num: nums){
            if (num<0){
                neg[n++] = num;
            }
            else{
                pos[p++] = num;
            }

        }

        int fp = 0;
        int fn = 0;

        int res[] = new int[l];
        for(int i = 0; i < l; i++){
            if (i % 2 == 0){
                res[i] = pos[fp++];
            }
            else{
                res[i] = neg[fn++];
            }
        }
        
        return res;
    }
}