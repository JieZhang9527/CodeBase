1. stringstream 

```C++
class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string ans, word;
        while(ss>>word){
            reverse(word.begin(),word.end());
            ans+=" "+word;
        }
        return ans.erase(0,1);
    }
};
```