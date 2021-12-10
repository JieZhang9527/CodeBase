1. 滑动窗口

```C++
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char,int> ump;
        for(auto c : s1)    ++ump[c];
        int left=0,right=0;
        while(right<s2.size()){
            char c=s2[right++];
            --ump[c];
            while(left<right&&ump[c]<0)
                ++ump[s2[left++]];
            if(right-left==s1.size())
                return true;
        }
        return false;
    }
};
```