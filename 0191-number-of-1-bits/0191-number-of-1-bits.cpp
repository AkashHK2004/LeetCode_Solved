class Solution {
public:
    int hammingWeight(uint32_t n) {
        int no_of_1_bits=0;
        while(n!=0){
            if(n&1){
                no_of_1_bits+=1;
                
            }
            n=n>>1;
            
        }
        return no_of_1_bits;
        
    }
};