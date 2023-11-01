class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i+1] - nums[i] == 2)
                return nums[i]+1;
        }
        int last = nums[nums.size()-1];
        if((nums.size() - last) == 1)
            return nums.size();
        else if((nums.size() - last) == 0)
            return 0;
        if(nums.size() == 1)
                return 0;
        
        return -1;
    }
};