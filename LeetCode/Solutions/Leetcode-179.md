1. STL排序
> 使用字符串比较，字符串大小比较和数字相同

```C++
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        if(nums.empty())    return string();
        vector<string> strs;
        for(auto num : nums)    strs.push_back(to_string(num));
        // !!! 这里的判断条件
        sort(strs.begin(),strs.end(),[](string &lhs, string &rhs){return lhs+rhs>rhs+lhs;});
        string ans=string();
        for(auto str : strs)    ans+=str;
        int index=0;
        for(;index<ans.size();++index){
            if(ans[index]!='0') break;
        }
        return index==ans.size()?"0":ans.substr(index);
    }
};
```