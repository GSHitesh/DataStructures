class Solution {
public:
    int findMin(vector<int>& A) {
        int l = 0;
        int h = A.size()-1;
        int mid;
        
        while(l+1<h){
             mid = (l+h)/2;
            if(A[mid] > A[h]){
                l = mid;                
                
            }
            else
                h = mid;
        }
        return min(A[l],A[h]);
    }
};