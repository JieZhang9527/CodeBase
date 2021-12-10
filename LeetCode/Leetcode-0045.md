1. 贪心算法

```C++
class Solution {
public:
    int jump(vector<int>& nums) {
        int ans=0;
        // 上一次跳跃能够到达的最远距离  当前位置跳跃能够到达的最远距离
        int pre_farthest=0, curr_farthest=0;
        // 如果达到最后一个位置则无需跳跃，因此-1
        for(int i=0;i<nums.size()-1;++i){
            curr_farthest=max(curr_farthest,nums[i]+i);
            // 在上次跳跃的最远位置，必须再跳一次才能达到下一个位置
            if(i==pre_farthest){
                pre_farthest=curr_farthest;
                ++ans;
            }
        }
        return ans;
    }
};
```