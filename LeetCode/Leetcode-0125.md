1. 双指针
> isalnum()判断是否为字母或数字
```C++
class Solution {
public:
    bool isPalindrome(string s) {
        int left=0, right=s.size()-1;
        while(left<right){
            while(left<right&&!isalnum(s[left]))    ++left;
            while(left<right&&!isalnum(s[right]))   --right;
            if(tolower(s[left])!=tolower(s[right]))   return false;
            ++left; --right;
        }
        return true;
    }
};
```