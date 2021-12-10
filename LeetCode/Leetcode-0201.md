> 与运算中只要有一方为0,则最终结果为0,从 m -> n 位从低到高变化,也就是说只要求解公共的高位,其余低位在与运算后都会变成0

1. 位运算
```C++
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int count=0;
        while(m!=n){
            m>>=1;
            n>>=1;
            ++count;
        }
        return m<<count;
    }
};
```

2. Brian Kernighan算法(布莱恩·柯林翰 算法)
> n & (n-1)  则n的二进制串中最右边的1将变为0,运用此算法求解两个二进制串的公共子串

```C++
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        while(m<n){
            n &= n-1;
            cout<<m<<" "<<n<<endl;
        }
        return m&n;
    }
};
```