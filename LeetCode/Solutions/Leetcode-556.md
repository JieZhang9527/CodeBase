1. 遍历

> 从低位向高位遍历，记录当前位前面的最大数，如果前面的低位中有数比当前位大，调换当前数和刚好大于当前数的低位数字，将低位数字重新排序
> 例子：  
> 12443322  
> 13222344


> 注意：有可能调换后的数超过32位整数，要添加判断语句

```C++
class Solution {
public:
    int nextGreaterElement(int n) {
        vector<int> nums;
        int duplicate=n;
        while(n){
            nums.push_back(n%10);
            n/=10;
        }
        reverse(nums.begin(),nums.end());
        if(nums.size()<=1)  return -1;
        for(int i=nums.size()-2;i>=0;--i){
            int index=-1, min_val=INT_MAX;
            for(int j=nums.size()-1;j>i;--j){
                if(nums[j]>nums[i]){
                    if(nums[j]<min_val){
                        min_val=nums[j];
                        index=j;
                    }
                }
            }
            if(index!=-1){
                swap(nums[i],nums[index]);
                sort(nums.begin()+i+1,nums.end());
                break;
            }
        }
        int ans=0;
        for(int i=0;i<nums.size();++i){
            if(ans>INT_MAX/10||(ans==INT_MAX/10&&nums[i]>7))    return -1;
            ans=ans*10+nums[i];
        }
        return ans==duplicate?-1:ans;
    }
};
```