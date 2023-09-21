class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        for (int i=0;i<nums.size()-1;i++){
            if(nums[i]==nums[i+1]){
                nums[i]+=nums[i+1];
                nums[i+1]=0;
            }

        }
        int j=0;
        for (int i=0;i<nums.size();i++){
            if(nums[i]!=0){
                nums[j]=nums[i];
                j+=1;
            }

        }
        while(j<nums.size()){
            nums[j]=0;
            j++;
        }
        return nums;
    }
};