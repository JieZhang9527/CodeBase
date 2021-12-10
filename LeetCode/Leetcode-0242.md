1. 遍历计数

```C++
class Solution {
public:
    bool isAnagram(string s, string t) {
        // 对应元素数量相同
        if(s.size()!=t.size())  return false;
        int alpha_a[26]={0};
        int alpha_b[26]={0};
        for(char c : s){
            alpha_a[c-'a']++;
        }
        for(char c : t){
            alpha_b[c-'a']++;
        }
        for(int i=0;i<26;i++){
            if(alpha_a[i]!=alpha_b[i])  return false;
        }
        return true;
    }
};
```