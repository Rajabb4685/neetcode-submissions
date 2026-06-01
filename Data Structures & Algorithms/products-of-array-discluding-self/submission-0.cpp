class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // Given array nums
        // return array output 
        // where output[i] is the products all numbers in array nums except the nums[i]

        // prefix 
        // postfix
        // result  

        int n = nums.size(); 
        vector<int> prefix(n);
        vector<int> postfix(n);
        vector<int> output(n);

        prefix[0] = 1;
        postfix[n-1] = 1;

        // prefix 
        // [1,2,3,4]
        // [1,1,2,6]
        for (int i = 1; i < n; i++){
            prefix[i] = nums[i-1] * prefix[i-1];
        }

        // postfix 
        // [1,2,3,4]
        // [24,12,4,1]
        for (int i = n - 2; i >= 0; i--){
            postfix[i] = nums[i+1] * postfix[i+1];
        }

        // output 
        // [1,2,3,4]
        // [24,12,8,6]
        for (int i = 0; i < n; i++){
            output[i] = prefix[i] * postfix[i];
        }
        return output;


        

    }
};
