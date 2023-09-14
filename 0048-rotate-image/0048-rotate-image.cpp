class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int start=0;
        int end=matrix.size()-1;
        
        while(start<=end){
            swap(matrix[start],matrix[end]);
            start++;
            end--;
        }
        
        
        for ( int i=0;i<matrix.size();i++){
            for (int j=0;j<i;j++){
                swap(matrix[i][j],matrix[j][i]);
            }
        }
    }
};