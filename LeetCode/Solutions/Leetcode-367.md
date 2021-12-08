1. 二分查找

> 除了1 2 3其他所有元素一半的平方都大于等于这个数，所以1要特殊判断

```C++
class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num==1)  return true;
        int left=0, right=num/2;
        // !!!
        while(left<=right){
            long long mid=(left+right)/2;
            long long temp=mid*mid;
            if(temp==num)   return true;
            else if(temp>num)   right=mid-1;
            else    left=mid+1;
        }
        return false;
    }
};
```

2. 牛顿法

```C++
class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num==1)  return true;
        long mid=num/2;
        while(mid*mid>num){
            mid=(mid+num/mid)/2;
        }
        return mid*mid==num;
    }
};
```