class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // return true/false - bool
        // array - nums 

        // nested loop 
        // first loop starts at the first value 
            // second loop starts at the next value after i (i+1)
                // if nums[i] == nums[j+1]
                    // return True 
        // return False 

        for (int i = 0; i < nums.size(); i++){ 
            for(int j = i; j < nums.size() - 1; j++){
                if(nums[i] == nums[j+1]){
                    return true;
                }
            }
        }
        return false;

        // time - o(n^2)
        // space - o(1)

       std::unordered_set<int> setValue(nums.begin(), nums.end());
       if (setValue.size() < nums.size()){
        return true;
       } else {
        return false;
       }
       





        
    }
};