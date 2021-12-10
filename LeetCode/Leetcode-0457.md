1. 快慢指针

> 解决数组或链表是否有环问题可以朝快慢指针上想

> 初始化快慢指针  
> 对每个起始位置开始遍历，如果当前值为0说明之前判断走不通
> 快慢指针遍历数组，因为不允许反向，因此除了快慢指针符号要相同，还要和快指针的下一个位置的数符号相同（因为快指针前进两步，如果不提前判断就无法判断快指针的前进一步时的符号）  
> 每次迭代最后，将慢指针经过的地方值变为0，说明已经遍历过并不可行

```C++
class Solution {
public:
    bool circularArrayLoop(vector<int>& nums) {
        for(int i=0;i<nums.size();++i){
            if(nums[i]==0)  continue;
            int slow=i,fast=next(nums,i);
            while(nums[slow]*nums[fast]>0&&nums[slow]*nums[next(nums,fast)]>0){
                if(slow==fast){
                    if(slow==next(nums,slow))  break;
                    return true;
                }
                slow=next(nums,slow);
                fast=next(nums,next(nums,fast));
            }
            slow=i;
            while(nums[i]*nums[slow]>0){
                nums[slow]=0;
                slow=next(nums,slow);
            }
        }
        return false;
    }
private:
    // next函数用于求取下一个位置索引，注意实现部分：索引i,有可能为正有可能为负
    int next(const vector<int> &nums,int i){
        int len=nums.size();
        int ans=((nums[i]+i)%len+len)%len;
        return ans;
    }
};
```