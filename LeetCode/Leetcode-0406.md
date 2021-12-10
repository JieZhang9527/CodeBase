1. 贪心算法

> 首先按照身高从大到小排序，身高相同的按照前面人数从小到大排序  
> 遍历vector，将每个人的信息按照前面的人数插入相关索引  
> 因为身高矮的插入到前面的排好序的高的人中不影响已排序相对位置

```C++
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(),people.end(),
        [](vector<int> &a, vector<int> &b){
            return a[0]!=b[0]?a[0]>b[0]:a[1]<b[1];
        });
        vector<vector<int>> ans;
        for(auto &vec : people) ans.insert(ans.begin()+vec[1],vec);
        return ans;
    }
};
```