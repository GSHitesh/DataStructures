class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        if(typed.size()<name.size())
        return false;
        if(typed == name)
        return true;
        int i,j;
        for(i = 0,j=0; i<name.size() && j<typed.size(); )
        {
            if(name[i] == typed[j])
            {
                i++;
                j++;
            }
            else
            if(j>0 && typed[j] == typed[j-1])
            j++;
            else
            return false;
        }
        while(j<typed.size())
        {
            if(typed[j]!=typed[j-1])
            return false;
            j++;
        }

        if(i>=name.size() && j>=typed.size())
        return true;

        return false;
    }
};