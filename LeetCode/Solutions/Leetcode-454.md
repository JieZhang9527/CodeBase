1. 哈希

> 以空间换时间，时空复杂度较高

```C++
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        vector<int> nums;
        unordered_map<int,int> ump;
        for(int i=0;i<A.size();++i){
            for(int j=0;j<B.size();++j){
                nums.push_back(A[i]+B[j]);
            }
        }
        for(int m=0;m<C.size();++m){
            for(int n=0;n<D.size();++n){
                ump[C[m]+D[n]]++;
            }
        }
        int ans=0;
        for(auto num : nums){
            if(ump.find(-num)!=ump.end())
                ans+=ump[-num];
        }
        return ans;
    }
};
```