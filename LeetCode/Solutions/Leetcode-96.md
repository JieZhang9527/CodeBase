1. 卡特兰特数
$$
C_0=1 \quad C_{n+1}=\frac{2(2n+1)}{n+2}C_n
$$

```C++
class Solution {
public:
    int numTrees(int n) {
        if(n==0)    return 0;
        long ans=1;
        for(int i=1;i<=n;++i){
            ans=2*ans*(2*i-1)/(i+1);
        }
        return (int)ans;
    }
};
```