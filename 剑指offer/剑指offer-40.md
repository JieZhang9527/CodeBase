1. priority_queue

> 小顶堆

```C++
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        priority_queue<int,vector<int>,greater<int>> pq;
        for(auto num : arr) pq.push(num);
        vector<int> ans;
        for(int i=0;i<k;++i){
            ans.push_back(pq.top());
            pq.pop();
        }
        return ans;
    }
};
```

2. 手撕堆排序

> 小顶堆

```C++
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        int heapSize=arr.size();
        vector<int> ans;
        if(k==heapSize) return arr; // 特殊判断，否则出错
        buildMinHeap(arr,heapSize);
        for(int i=arr.size()-1;i>=arr.size()-k;--i){
            ans.push_back(arr[0]);
            swap(arr[0],arr[i]);
            --heapSize;
            minHeapify(arr,0,heapSize);
        }
        return ans;
    }
private:
    void minHeapify(vector<int> &arr, int i, int heapSize){
        int left=2*i+1, right=2*i+2, least=i;
        if(left<heapSize&&arr[left]<arr[least]) least=left;
        if(right<heapSize&&arr[right]<arr[least])   least=right;
        if(least!=i){
            swap(arr[least],arr[i]);
            // !!!向下调整堆的时候，swap交换值但没有改变索引
            minHeapify(arr,least,heapSize);
        }
    }
    void buildMinHeap(vector<int> &arr, int heapSize){
        for(int i=heapSize/2;i>=0;--i){
            minHeapify(arr,i,heapSize);
        }
    }
};
```

> 大顶堆，求解最大的K个数

```C++
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        int heapSize=arr.size();
        vector<int> ans;
        if(k==heapSize) return arr; // 特殊判断，否则出错
        buildMaxHeap(arr,heapSize);
        for(int i=arr.size()-1;i>=arr.size()-k;--i){
            ans.push_back(arr[0]);
            swap(arr[0],arr[i]);
            --heapSize;
            maxHeapify(arr,0,heapSize);
        }
        return ans;
    }
private:
    void maxHeapify(vector<int> &arr, int i, int heapSize){
        int left=2*i+1, right=2*i+2, largest=i;
        if(left<heapSize&&arr[left]>arr[largest])   largest=left;
        if(right<heapSize&&arr[right]>arr[largest]) largest=right;
        if(largest!=i){
            swap(arr[i],arr[largest]);
            maxHeapify(arr,largest,heapSize);
        }
    }
    void buildMaxHeap(vector<int> &arr, int heapSize){
        for(int i=heapSize/2;i>=0;--i){
            maxHeapify(arr,i,heapSize);
        }
    }
};
```

3. 快速排序

```C++
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        vector<int> ans;
        if(k==0)    return ans; // 特殊判断 
        if(k==arr.size())   return arr;
        int left=0, right=arr.size()-1;
        while(true){
            int index=partition(arr,left,right);
            if(index==k-1) break;
            else if(index>k-1)  right=index-1;
            else    left=index+1;
        }
        copy(arr.begin(),arr.begin()+k,back_inserter(ans));
        return ans;
    }
private:
    int partition(vector<int> &arr, int left, int right){
        swap(arr[left],arr[rand()%(right-left+1)+left]);
        int pivot=arr[left];
        while(left<right){
            while(left<right&&arr[right]>=pivot)    --right;
            swap(arr[left],arr[right]);
            while(left<right&&arr[left]<=pivot) ++left;
            swap(arr[left],arr[right]);
        }
        arr[left]=pivot;
        return left;
    }
};
```