1. 二分查找

```C++
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left=1,right=n;
        while(left<right){
            int mid=left/2+right/2+(left%2+right%2)/2;
            if(!isBadVersion(mid))  left=mid+1;
            if(isBadVersion(mid))   right=mid;
        }
        return right;
    }
};
```