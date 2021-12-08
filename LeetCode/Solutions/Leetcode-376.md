1. dp

> 每当我们选择一个元素作为摆动序列的一部分时，这个元素要么是上升的，要么是下降的，这取决于前一个元素的大小。  
> up[i] 是目前为止最长的以第 i 个元素结尾的上升摆动序列的长度。  
> down[i] 记录的是目前为止最长的以第 i 个元素结尾的下降摆动序列的长度

```C++
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.size()<2)    return nums.size();
        vector<int> up(nums.size(),0), down(nums.size(),0);
        up[0]=1; down[0]=1;
        for(int i=1;i<nums.size();++i){
            for(int j=0;j<i;++j){
                if(nums[i]>nums[j]) up[i]=max(up[i],down[j]+1);
                else if(nums[i]<nums[j]) down[i]=max(down[i],up[j]+1);
                // 注意处理相等的情况
                else{
                    up[i]=max(up[i],up[j]);
                    down[i]=max(down[i],down[j]);
                }
            }
        }
        return max(up.back(),down.back());
    }
};
```

2. 线性dp

> 其实并不需要双层循环

```C++
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.size()<2)    return nums.size();
        vector<int> up(nums.size(),0), down(nums.size(),0);
        up[0]=1; down[0]=1;
        for(int i=1;i<nums.size();++i){
            if(nums[i]>nums[i-1]){
                up[i]=down[i-1]+1;
                down[i]=down[i-1];
            }
            else if(nums[i]<nums[i-1]){
                down[i]=up[i-1]+1;
                up[i]=up[i-1];
            }
            else{
                down[i]=down[i-1];
                up[i]=up[i-1];
            }
        }
        return max(up.back(),down.back());
    }
};
```

3. 记忆化dp

> 上述dp中每次只用到上一个状态，因此可缩减删的

```C++
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.size()<2)    return nums.size();
        int up=1, down=1;
        for(int i=1;i<nums.size();++i){
            if(nums[i]>nums[i-1])   up=down+1;
            else if(nums[i]<nums[i-1])  down=up+1;
        }
        return max(up,down);
    }
};
```