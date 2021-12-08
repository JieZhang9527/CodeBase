1. 保存和数组

```C++
class NumArray {

public:
    NumArray(vector<int>& nums) {
        int sum=0;
        for(auto num : nums){
            sum+=num;
            sums.push_back(sum);
        }
    }
    int sumRange(int i, int j) {
        if(i==0)    return sums[j];
        return sums[j]-sums[i-1];
    }
    vector<int> sums;
};
```