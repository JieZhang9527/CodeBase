topk问题
1. 快速排序
> 快速排序中，通过一次partition操作可以将一个数字放置在最终位置上，可以利用该特性提前退出

```C++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int left=0, right=nums.size()-1;
        int target=nums.size()-k;
        while(true){
            int index=partition(nums,left,right);
            if(index==target)   return nums[index];
            else if(index>target)   right=index-1;
            else    left=index+1;
        }
        return -1;
    }
private:
    int partition(vector<int> &nums, int left, int right){
        swap(nums[left],nums[rand()%(right-left+1)+left]);
        int pivot=nums[left];
        while(left<right){
            while(left<right&&nums[right]>=pivot)   --right;
            swap(nums[left],nums[right]);
            while(left<right&&nums[left]<=pivot)    ++left;
            swap(nums[left],nums[right]);
        }
        nums[left]=pivot;
        return left;
    }
};
```

2. 堆排序

> 使用STL中的优先队列

```C++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return k>nums.size()/2?lessHeap(nums,nums.size()-k+1):greaterHeap(nums,k);
    }
private:
    int greaterHeap(vector<int> &nums, int k){
        priority_queue<int,vector<int>,greater<int>> pq;
        for(auto num : nums){
            if(pq.size()==k){
                if(pq.top()>=num)   continue;
                else    pq.pop();
            }
            pq.push(num);
        }
        return pq.top();
    }
    int lessHeap(vector<int> &nums, int k){
        priority_queue<int,vector<int>, less<int>> pq;
        for(auto num : nums){
            if(pq.size()==k){
                if(pq.top()<=num)   continue;
                else    pq.pop();
            }
            pq.push(num);
        }
        return pq.top();
    }
};
```

> 手写堆排序

```C+
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int heapSize=nums.size();
        buildMaxHeap(nums,heapSize);
        for(int i=nums.size()-1;i>=nums.size()-k+1;--i){
            swap(nums[0],nums[i]);
            --heapSize;
            maxHeapify(nums,0,heapSize);
        }
        return nums[0];
    }
private:
    void maxHeapify(vector<int> &nums, int index, int heapSize){
        int left=index*2+1, right=index*2+2, largest=index;
        if(left<heapSize&&nums[left]>nums[largest]) largest=left;
        if(right<heapSize&&nums[right]>nums[largest])   largest=right;
        if(largest!=index){
            swap(nums[index],nums[largest]);
            maxHeapify(nums,largest,heapSize);
        }
    }
    // 从底向上调整
    void buildMaxHeap(vector<int> &nums, int heapSize){
        for(int i=heapSize/2;i>=0;--i){
            maxHeapify(nums,i,heapSize);
        }
    }
};
```