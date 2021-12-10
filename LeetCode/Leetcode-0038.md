1. 模拟
> 遍历上一字符串每个元素的个数

```C++
class Solution {
public:
    string countAndSay(int n) {
        string pre="1", curr="";
        for(int i=2;i<=n;++i){
            int count=0;
            // 当前需要计数的字符串
            char temp=pre[0];
            for(int j=0;j<pre.size();++j){
                if(pre[j]==temp)    ++count;
                else{
                    curr+=to_string(count)+temp;
                    temp=pre[j];
                    count=1;
                }
            }
            curr+=to_string(count)+temp;
            pre=curr;
            curr="";
        }
        return pre;
    }
};
```