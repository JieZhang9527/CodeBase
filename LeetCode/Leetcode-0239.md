1. 单调队列

> O(1)时间获取窗口的最大值  
> 设计单调递减队列数据结构，当前窗口内的最大值即为队头元素

```C++
class DecreaseQue{
public:
    void push(int val){
        while(!dq.empty()&&dq.back()<val) dq.pop_back();
        dq.push_back(val);
    }
    void pop(int val){
        if(!dq.empty()&&dq.front()==val)  dq.pop_front();
    }
    int max(){
        return dq.front();
    }
private:
    deque<int> dq;
};

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        DecreaseQue q;
        for(int i=0;i<nums.size();++i){
            if(i<k-1)   q.push(nums[i]);
            else{
                q.push(nums[i]);
                ans.push_back(q.max());
                q.pop(nums[i-k+1]);
            }
        }
        return ans;
    }
};
```