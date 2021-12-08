1. 双指针法

```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int index1=0, index2=numbers.size()-1;
        int sum=numbers[index1]+numbers[index2];
        while(sum!=target&&index1<index2){
            if(sum<target)  ++index1;
            else    --index2;
            // 注意更新sum值的位置
            sum=numbers[index1]+numbers[index2];
        }
        vector<int> ans={index1+1,index2+1};
        return ans;
    }
};
```