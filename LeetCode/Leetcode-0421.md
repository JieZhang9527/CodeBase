1. 位运算

> 从二进制的高位到低位遍历获得是否有满足该位异或为1的组合

```C++
class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int max_val=*(max_element(nums.begin(),nums.end()));
        int len=0;  //最大数二进制表示的长度
        while(max_val){
            max_val >>= 1;
            ++len;
        }
        int ans=0,curr=0;
        for(int i=len-1;i>=0;--i){
            ans <<= 1;
            curr = ans | 1;
            unordered_set<int> prefixes;
            for(auto num : nums)    prefixes.insert(num >> i);
            for(auto it : prefixes){
                if(prefixes.find(curr ^ it)!=prefixes.end()){
                    ans = curr;
                    break;
                }
            }
        }
        return ans;
    }
};
```