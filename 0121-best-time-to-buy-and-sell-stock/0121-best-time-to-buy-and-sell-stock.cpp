class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int l=0;
        int r=1;
        int ans=0;
        int profit=0;
        while(r<prices.size()){
            profit=prices[r]-prices[l];
            if(prices[l]<prices[r]){
                ans=max(profit,ans);
            
            }
            else{
                l=r;
            }
            r+=1;
        }
        return ans;
        
    }
};