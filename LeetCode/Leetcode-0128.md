1. 哈希
> 利用set有序的特点

```C++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty())    return 0;
        set<int> st;
        for(auto num : nums)    st.insert(num);
        int ans=1, count=1, pre=*(st.begin());
        auto iter=st.begin();
        for(++iter;iter!=st.end();++iter){
            if(*iter==pre+1)    ++count;
            else{
                ans=max(ans,count);
                count=1;
            }
            pre=*iter;
        }
        ans=max(ans,count);
        return ans;
    }
};
```