1. 二分查找

```C++
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int left=1,right=n;
        int mid;
        int flag;
        while(left<=right){
            mid=left+(right-left)/2;   //这一点需要特别注意，很可能上溢出
            flag=guess(mid);
            if(flag==0)  return mid;
            else if(flag==1)  left=mid+1;
            else  right=mid-1;
        }
        return -1;
    }
};
```