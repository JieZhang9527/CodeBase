1. 位运算
> 十进制数转为二进制，出现次数为3次的数字的各个二进制位1的个数也为3的倍数  
>  因此可以统计所有数字二进制位中1的个数，并对3求余数

```C++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int count[32]={};
        for(auto num : nums){
            for(int i=0;i<32;++i){
                count[i]+=num & 1;
                num >>= 1;
            }
        }
        int ans=0;
        for(int i=31;i>=0;--i){
            ans <<= 1;
            ans |= count[i]%3;
        }
        return ans;
    }
};
```

2. 数学规律
> 3×(a+b+c)−(a+a+a+b+b+b+c)=2c  
> 注意溢出问题

```C++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_set<int> ust;
        long sum_ust=0, sum_vec=0;
        for(auto num : nums){
            if(ust.find(num)==ust.end()){
                ust.insert(num);
                sum_ust+=num;
            }
            sum_vec+=num;
        }
        return (sum_ust*3-sum_vec)/2;
    }
};
```