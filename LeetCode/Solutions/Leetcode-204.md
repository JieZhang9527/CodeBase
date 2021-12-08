1. 埃氏筛选法
> 从小到大枚举所有的数,如果一个数是素数,那么这个数的倍数肯定不是素数,当到达某个数时,如果这个数没有被前面的数筛去,那么肯定是素数

```C++
class Solution {
public:
    int countPrimes(int n) {
        vector<int> ans;
        vector<bool> prime(n,true);
        for(int i=2;i<n;++i){
            if(prime[i]){
                ans.push_back(prime[i]);
                for(int j=i+i;j<n;j+=i) prime[j]=false;
            }
        }
        return ans.size();
    }
};
```
