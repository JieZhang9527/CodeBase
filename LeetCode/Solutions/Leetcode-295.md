1. 堆

```C++
class MedianFinder {
public:
    MedianFinder() {

    }
    
    void addNum(int num) {
        maxHeap.push(num);  // 保证数据有序
        minHeap.push(maxHeap.top());
        maxHeap.pop();
        if(maxHeap.size()<minHeap.size()){
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    
    double findMedian() {
        if(maxHeap.size()>minHeap.size())   return double(maxHeap.top());
        else    return (maxHeap.top()+minHeap.top())/2.0;
    }
private:
    // 升序队列，小根堆
    priority_queue<int,vector<int>,greater<int>> minHeap;
    // 降序队列，大根堆
    priority_queue<int,vector<int>,less<int>> maxHeap;
};
```
