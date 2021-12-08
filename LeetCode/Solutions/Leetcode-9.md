1. 逐个比对对应位

```C++
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        vector<int> nums;
        while(x){
            nums.push_back(x%10);
            x/=10;
        }
        int left=0, right=nums.size()-1;
        while(left<right){
            if(nums[left]!=nums[right]) return false;
            ++left;
            --right;
        }
        return true;
    }
};
```