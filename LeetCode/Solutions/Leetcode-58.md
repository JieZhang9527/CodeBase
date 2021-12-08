1. ``stringstream``
> ``stringstream``可以简化字符串的空格处理

```C++
class Solution {
public:
    int lengthOfLastWord(string s) {
        stringstream ss(s);
        int ans=0;
        string word=string();
        while(ss>>word) ans=word.size();
        return ans;
    }
};
```