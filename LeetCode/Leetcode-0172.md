1. 分解质因数
> 先把阶乘算出来再计算很容易溢出  
> 本题实质是一个数学问题:分解质因数，只有质因数$2*5=10$才会得到一个0，每隔两个数就会出现一个2,每隔四个数就会多出一个2(4=2*2)，每隔五个数才会多出一个5,每隔25个数才会多出一个5, 因此5的个数少于等于2的个数,只要统计质因数5的个数即可
> $$
> count=n/5+n/25+n/125......=n/5+n/5/5+n/5/5/5....
> $$

```C++
class Solution {
public:
    int trailingZeroes(int n) {
        int count=0;
        while(n){
            count+=n/5;
            n/=5;
        }
        return count;
    }
};
```