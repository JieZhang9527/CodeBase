1. 贪心算法

> 在首尾分别加上一个0，处理数组开头就和处理中间一致了

```C++
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        flowerbed.insert(flowerbed.begin(),0);
        flowerbed.insert(flowerbed.end(),0);
        int count=0;
        for(int mid=1;mid<flowerbed.size()-1;++mid){
            if(flowerbed[mid]==0&&flowerbed[mid-1]==0&&flowerbed[mid+1]==0){
                flowerbed[mid]=1;
                ++count;
            }
        }
        return count>=n;
    }
};
```