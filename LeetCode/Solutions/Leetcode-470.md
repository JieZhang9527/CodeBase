> 如何从Rand10生成Rand7？  
> Rand10生成的每个数概率都是相同的，如果我们将[8,10]范围内的数舍去，[1-7]中每个数获得的概率相等，就获得了Rand7


> 从Rand7生成Rand10的思路类似，先获得较大的数，然后删减去超出范围的数:  
> ((Rand7-1)*7)+Rand7  
> Rand7-1              0 1  2  3  4  5  6  
> (Rand7-1)*7          0 7 14 21 28 35 42  
> ((Rand7-1)*7)+Rand7  0 1  2  3  4  5  6  7 8 9 10 …… 48  
> [0,48]每个数出现的概率都是相等的,时间复杂度较高的原因是：删去了太多的数

```C++
class Solution {
public:
    int rand10() {
        int ans=0;
        while(true){
            ans=(rand7()-1)*7+rand7();
            if(ans<=10) break;
        }
        return ans;
    }
};
```

> 改进：只删除[41,49]

```C++
class Solution {
public:
    int rand10() {
        int num=(rand7()-1)*7+rand7();
        while(num>40){
            num=(rand7()-1)*7+rand7();
        }
        return num%10+1;
    }
};
**```**