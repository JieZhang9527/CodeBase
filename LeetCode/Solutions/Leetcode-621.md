1. 贪心算法

> 优先选择任务数多的执行
如果当前选择的任务已经为n+1,那么停止选择,重新排序选择任务数最多的
这样可以避免AAAAAAABCDEG n=2 这样的错误

```C++
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> nums(26,0);
        for(auto task : tasks)  nums[task-'A']++;
        int count=tasks.size();
        int ans=0;
        while(count){
            sort(nums.begin(),nums.end(),[](const int &a,const int &b){return a>b;});
            int num=0;
            for(int i=0;i<26;++i){
                if(nums[i]!=0){
                    nums[i]--;
                    ++num;
                }
                if(num==n+1)    break;
            }
            count-=num;
            if(num<n+1&&count)  ans+=n+1;
            else    ans+=num;
        }
        return ans;
    }
};
```