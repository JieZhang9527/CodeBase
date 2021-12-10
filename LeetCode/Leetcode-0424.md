1. 滑动窗口
   
> k>0 时，问题的实质就是如何求解当前滑动窗口中最多字母的个数。count用来记录当前滑动窗口中的最多的字母的个数，record数组用于维护滑动窗口中每个字母的个数。

```C++
class Solution {
public:
    int characterReplacement(string s, int k) {
        int left, right=0;
        int count=0;
        vector<int> record(128,0);
        int ans=0;
        while(right<s.size()){
            record[s[right]]++;
            count=max(count,record[s[right]]);
            while(count+k<right-left+1){
                record[s[left]]--;
                ++left;
            }
            ans=max(ans,right-left+1);
            ++right;
        }
        return ans;
    }
};
```