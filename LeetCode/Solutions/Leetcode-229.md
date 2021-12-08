1. 投票法

> 出现次数超过n/3的数字最多只有两个，其他的数加起来也不会超过它俩任何一个,每次拿走不一样的三个数，最后剩下的就是目标值

```C++
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> ans;
        if(nums.empty())    return ans;
        int candidate1=0,candidate2=0;
        int count1=0,count2=0;
        for(int num : nums){
            if(num==candidate1)  ++count1;
            else if(num==candidate2)  ++count2;
            else if(count1==0){
                candidate1=num;
                count1=1;
            }
            else if(count2==0){
                candidate2=num;
                count2=1;
            }
            else{
                --count1;
                --count2;
            }
        }
        count1=0;count2=0;
        for(int num : nums){
            if(num==candidate1)  ++count1;
            //关键是加 else if 而不是 if
            //否则 输入[0,0,0] 输出会变为[0,0]
            else if(num==candidate2)  ++count2;
        }
        if(count1>length/3) ans.push_back(candidate1);
        if(count2>length/3) ans.push_back(candidate2);
        return ans;
    }
};
```