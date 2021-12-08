1. 贪心算法

> 优先选择较大的饼干分给胃口较大的孩子

```C++
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int index_g=g.size()-1, index_s=s.size()-1;
        int ans=0;
        while(index_g>=0&&index_s>=0){
            if(s[index_s]>=g[index_g]){
                --index_g;
                --index_s;
                ++ans;
            }
            else    --index_g;
        }
        return ans;
    }
};
```