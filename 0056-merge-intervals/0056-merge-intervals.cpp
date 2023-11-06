class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        vector<vector<int>> newintervals;
        
        if(intervals.size() <= 1)
            return intervals;
        
        sort(intervals.begin(),intervals.end());
        
        newintervals.push_back(intervals[0]);
        int n = intervals.size();
        int j = 0;
               
        for(int i=1;i<n;i++){
            if(newintervals[j][1] >= intervals[i][0]){
                newintervals[j][1] = max(newintervals[j][1],intervals[i][1]);
            }
            else{
                j++;
                newintervals.push_back(intervals[i]);
            }
        }
        return newintervals;
    }
};