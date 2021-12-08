1. 26进制转10进制
```C++
class Solution {
public:
    int titleToNumber(string s) {
        int ans=0, weight=1;
        for(int i=s.size()-1;i>=0;--i){
            ans+=(s[i]-'A'+1)*weight;
            if(i==0)    break;  // 避免*26导致整数溢出
            weight=weight*26;
        }
        return ans;
    }
};
```