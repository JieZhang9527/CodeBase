1. 贪心算法

> [D1 D2 D3……]如果D2<D1 我们应该删除D1，如果没找到，就删除最末尾元素
每次删除都将问题转化为一个更小的子问题

```C++
class Solution {
public:
    string removeKdigits(string num, int k) {
        string ans=string();
        int len=num.size()-k;
        for(int i=0;i<num.size();++i){
            // 优先删除前面的大值
            while(k&&!ans.empty()&&num[i]<ans.back()){
                ans.erase(ans.end()-1);
                --k;
            }
            ans.push_back(num[i]);
        }
        ans.resize(len);
        while(!ans.empty()&&ans[0]=='0')
            ans.erase(ans.begin());
        if(ans.size()==0) return string("0");
        return ans;
    }
};
```