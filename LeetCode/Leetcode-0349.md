1. 双指针

> 排序时间复杂度较高

```C++
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        int index1=0, index2=0;
        while(index1<nums1.size()&&index2<nums2.size()){
            if(nums1[index1]==nums2[index2]){
                if(ans.empty()||ans.back()!=nums1[index1])   
                    ans.push_back(nums1[index1]);
                ++index1;   ++index2;
            }
            else if(nums1[index1]<nums2[index2])    ++index1;
            else    ++index2;
        }
        return ans;
    }
};
```