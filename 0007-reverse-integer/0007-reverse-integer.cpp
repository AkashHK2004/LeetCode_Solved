class Solution {
public:
    int reverse(int x) {
        int reverse_int=0;
        
        while(x!=0){
            int a=x%10;
            if (reverse_int<(INT_MIN/10)|| reverse_int>(INT_MAX/10)){
                return 0;
            }
            reverse_int=(reverse_int*10)+a;
            x=x/10;

        
        }
        return reverse_int;
        
    }
};