1. 遍历

> 从后向前遍历，count计算目前被计入引用的论文数

```C++
class Solution {
public:
    int hIndex(vector<int>& citations) {
        if(citations.empty())  return 0;
        sort(citations.begin(),citations.end());
        int count=0;
        for(int i=citations.size()-1;i>=0;--i){
            if(citations[i]>count)  ++count;
            else break;
        }
        return count;
    }
};
```