class Solution {
public:
    bool isPalindrome(string s) {
        string a="";
        int n = s.length();
        for(int i=0;i<n;i++){
            if(isalnum(s[i])){
                a += tolower(s[i]); 
            }
        }
        string b = a;
        reverse(b.begin(),b.end());
        
        
        if(a == b || a.empty())
            return 1;
        else
            return 0;
    }
};