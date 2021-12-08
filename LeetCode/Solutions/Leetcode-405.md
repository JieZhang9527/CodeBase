1. 位运算

> 每四位二进制对应一位十六进制

```C++
class Solution {
public:
    string toHex(int num) {
        string ans=string();
        if(num==0)  return "0";
        string hex="0123456789abcdef";
        // 对负数右移不会变为0
        while(num&&ans.size()<8){
            ans=hex[num&0xf]+ans;
            num>>=4;
        }
        return ans;
    }
};
```