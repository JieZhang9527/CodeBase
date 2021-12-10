1. 贪心算法
> 整数转罗马数字遵循：总是想用尽量大的罗马数字表达这个数，所以index先从大的数开始遍历

```C++
class Solution {
public:
    string intToRoman(int num) {
        int nums[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string romans[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string ans="";
        int index=0;
        while(index<13){
            while(num>=nums[index]){
                ans+=romans[index];
                num-=nums[index];
            }
            index++;
        }
        return ans;
    }
};
```
