1. 位运算

```C++
class Solution {
public:
    int hammingDistance(int x, int y) {
        int temp= x ^ y;
        int ans=0;
        while(temp){
            ans += temp & 1;
            temp >>= 1;
        }
        return ans;
    }
};
```

```C++
class Solution {
public:
    int hammingDistance(int x, int y) {
        int temp= x ^ y;
        int ans=0;
        while(temp){
            temp=temp&(temp-1);
            ++ans;
        }
        return ans;
    }
};
```