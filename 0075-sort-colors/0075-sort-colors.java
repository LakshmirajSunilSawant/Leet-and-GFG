class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length;
        int low = 0;
        int mid = 0;
        int high = n - 1;

        while (mid <= high){
            if(nums[mid] == 2){
                int temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;
                high -= 1;
            }
            else if(nums[mid] == 0){
                int temp1 = nums[mid];
                nums[mid] = nums[low];
                nums[low] = temp1;
                mid += 1;
                low += 1;
            }

            else{
                mid += 1;
            }
        }
        return;


    }
}