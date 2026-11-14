class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        int longest = 0;

        if(nums.length == 0){
            return 0;
        }

        for (int i = 0; i < nums.length; i++){
            set.add(nums[i]);
        }

        for (int num:set){
            if (set.contains(num-1)){
                continue;
            }
            else{
                int currnum = num;
                int currsub = 1;
                while (set.contains(currnum+1)){
                    currnum++;
                    currsub++;
                }
                longest = Math.max(longest,currsub);
            }
        }
        
        return longest;
       

    }
}