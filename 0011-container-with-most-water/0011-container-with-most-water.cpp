class Solution {
public:
    int maxArea(vector<int>& height) {
        int low = 0;
        int high = height.size()-1;
        int maxArea = INT_MIN;
        while(low<high){
            if(height[low] < height[high]){
                maxArea = max(maxArea, height[low]*(high-low));
                low++;
            }
            else{
                maxArea = max(maxArea, height[high]*(high-low));
                high--;
            }
            
        }
        
        return maxArea;
    }
};