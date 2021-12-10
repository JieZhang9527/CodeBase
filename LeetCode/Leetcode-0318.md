1. 位运算

> int 的二进制一共有32位,一共有26个字母,因此我们用每一位代表一个字母是否出现过
0表示没出现，1表示出现。  
> "abcd"二进制表示00000000 00000000 00000000 00001111  
> "bc"二进制表示00000000 00000000 00000000 00000110  
> 当两个字符串没有相同的字母时，二进制数与的结果为0。

```C++
class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector<int> binary(words.size(),0);
        for(int i=0;i<words.size();++i){
            for(int j=0;j<words[i].size();++j){
                binary[i] |= 1 << (words[i][j]-'a');
            }
        }
        int ans=0;
        for(int i=0;i<words.size();++i){
            for(int j=i+1;j<words.size();++j){
                if((binary[i] & binary[j])==0){
                    int temp=words[i].size() * words[j].size();
                    ans=max(ans,temp);
                }
            }
        }
        return ans;
    }
};
```