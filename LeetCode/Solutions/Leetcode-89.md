1. 获取格雷码
> 假设n阶格雷码序列为G(n)，获取G(n+1)方法为：
> - G(n)每个格雷码前加0，得到G'(n)
> - 设G(n)的逆序为R(n)，R(n)中每个序列前加上1得到R'(n)
> - G(n+1)=G'(n) U R'(n)

| n=0 | n=1 | n=2 | n=3 | n=4 |
| :-: | :-: | :-: | :-: | :-: |
|0|0|00|000| $\dots$ 
| |**1**|01|001| $\dots$
| | |**11**|011| $\dots$
| | |**10**|010| $\dots$
| | | |**110**|$\dots$
| | | |**111**|$\dots$
| | | |**101**|$\dots$
| | | |**100**|$\dots$

```C++
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> ans={0};
        // 权值，加到序列最前面的1
        int weight=1;
        for(int i=0;i<n;++i){
            for(int j=ans.size()-1;j>=0;--j)
                ans.push_back(ans[j]+weight);
            weight*=2;
        }
        return ans;
    }
};
```