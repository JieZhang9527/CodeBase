1. lamda表达式

```C++
class Solution {
public:
    string frequencySort(string s) {
        vector<int> count(128,0);
        for(auto c : s) count[c]++;
        sort(s.begin(),s.end(),[&count](char &a, char &b){
            return count[a]==count[b]?a<b:count[a]>count[b];
            });
        return s;
    }
};
```