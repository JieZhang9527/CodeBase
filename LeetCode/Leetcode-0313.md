1. 堆

> 起始先将最小丑数 1 放入队列  
> 每次从队列取出最小值，然后将最小值所对应的丑数x∗primes[i]进行入队

> 超时

```C++
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        unordered_set<long> ust;
        priority_queue<long,vector<long>,greater<long>> pq;
        pq.push(1L); ust.insert(1L);
        for(int i=1;i<n;++i){
            long temp=pq.top(); pq.pop();
            for(int prime : primes){
                long val=temp*prime;
                if(ust.find(val)==ust.end()){
                    ust.insert(val);
                    pq.push(val);
                }
            }
        }
        return pq.top();
    }
};
```