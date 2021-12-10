1. 位操作

```C++
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans=0;
        for(int i=0;i<32;++i){
            auto temp = (n >> i) & 1;
            ans = ans<<1 | temp;
        }
        return ans;
    }
};
```