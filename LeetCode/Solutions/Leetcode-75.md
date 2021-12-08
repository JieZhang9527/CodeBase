1. 荷兰国旗问题
> 用三个指针分别追踪0的右边界、当前遍历节点、2的左边界
> - 如果当前值等于0，和左边界交换
> - 如果当前值等于2，和右边界交换

> 注意curr的变化:   
> 如果是等于0和左边界交换,curr左边的值已经扫描过了,因此可以++curr  
> 如果是等于2和右边界交换,右边的还没有扫描过,因此要再次扫描是不是与左边的交换,不能++curr

```C++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int idx0_right=0, idx2_left=nums.size()-1, idx_curr=0;
        while(idx_curr<=idx2_left){
            if(nums[idx_curr]==0){
                swap(nums[idx0_right],nums[idx_curr]);
                ++idx0_right;
                ++idx_curr; // 左边交换的值不
            }
            else if(nums[idx_curr]==2){
                swap(nums[idx2_left],nums[idx_curr]);
                --idx2_left;
            }
            else    ++idx_curr;
        }
    }
};
```

2. 快速排序

```C++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        quickSort(nums,0,nums.size()-1);
    }
    void quickSort(vector<int> &nums,int left,int right){
        if(left>=right) return;
        int index=partition(nums,left,right);
        quickSort(nums,left,index-1);
        quickSort(nums,index+1,right);
    }
    int partition(vector<int> &nums,int left,int right){
        int pivot=nums[left];
        while(left<right){
            while(left<right && nums[right]>=pivot) --right;
            swap(nums[left],nums[right]);
            while(left<right && nums[left]<=pivot)  ++left;
            swap(nums[left],nums[right]);
        }   
        nums[left]=pivot;
        return left;
    }
};
```