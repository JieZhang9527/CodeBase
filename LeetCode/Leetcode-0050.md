1. 快速幂
> 本题采用暴力计算会超时。如果我们知道$x^N$，可通过$(x^N)^2$直接求解$x^{2N}$，而不用一次次相乘，时空复杂度降为$O(logN)$  
> 注意：INT_MIN转为正数时会溢出，必须特殊处理或使用long处理

```C++
class Solution {
public:
    double myPow(double x, int n) {
        long temp=n;
        if(n<0){
            x=1/x;
            temp=-temp;
        }
        return fastPow(x,temp);
    }
private:    
    double fastPow(double x, int n){
        if(n==0)    return 1.0;
        double half=fastPow(x,n/2);
        return n%2?half*half*x:half*half;
    }
};
```