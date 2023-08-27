class Solution {
public:
    int subtractProductAndSum(int n) {
        int product=1;
        int sum=0;
        while(n!=0){
            int a=n%10;
            sum+=a;
            product*=a;
            n=n/10;
        }
        int ans=(product-sum);
        return ans ;
        
    }
};