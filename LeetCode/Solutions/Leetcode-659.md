1. 贪心算法

> count用于记录每个数字的个数、tail用于记录以某个数字结尾的符合长度要求的序列的个数

> 如果当前数字已经被前面的序列用过,直接跳过  
> 如果当前数字没被用过并且可以接到一个相关序列满足要求,则该数字个数减一,变动相应的尾  
> 如果当前数字可以和接下来连续的两个数构成满足要求的序列,则相关数字的个数减一,尾变化
> 否则,该数字不能构成符合条件序列的一部分

```C++
class Solution {
public:
    bool isPossible(vector<int>& nums) {
        unordered_map<int,int> count,tail;
        for(auto num : nums)    count[num]++;
        for(auto num : nums){
            if(count[num]==0)   continue;
            else if(count[num]>0&&tail[num-1]>0){
                count[num]--;
                tail[num-1]--;
                tail[num]++;
            }
            else if(count[num]>0&&count[num+1]>0&&count[num+2]>0){
                count[num]--;
                count[num+1]--;
                count[num+2]--;
                tail[num+2]++;
            }
            else    return false;
        }
        return true;
    }
};
```