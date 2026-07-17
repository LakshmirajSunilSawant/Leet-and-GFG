class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();

        int m = matrix.length;
        int n = matrix[0].length;


        int top =0;
        int bottom = m-1;
        int left = 0;
        int right = n - 1;

        while (top <= bottom && left <= right){
            for(int i = left; i <= right; i++){
                ans.add(matrix[top][i]);
            }
            top++;

            for(int j = top; j <= bottom; j++){
                ans.add(matrix[j][right]);
            }
            right--;
            if(top <= bottom){
                for(int d = right ; d >= left; d--){
                    ans.add(matrix[bottom][d]);
                }
                bottom--;
            }
            if(left <= right){
                for(int k = bottom; k >= top; k--){
                    ans.add(matrix[k][left]);
                }
                left++;
            }
            
        }
        return ans;
    }
}