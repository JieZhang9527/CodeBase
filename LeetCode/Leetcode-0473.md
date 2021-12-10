1. 回溯

> 将i根火柴分别加入四条边中，对每种放置方法再放i+1根火柴

```C++
class Solution {
public:
    bool makesquare(vector<int>& nums) {
        int perimeter=accumulate(nums.begin(),nums.end(),0);
        if(nums.empty()||perimeter%4)  return false;
        int side=perimeter/4;
        sort(nums.begin(),nums.end(),[](const int &a,const int &b){return a>b;});
        vector<int> sides(4,0);
        return DFS(nums,0,side,sides);
    }
private:
    bool DFS(const vector<int> &nums,int index,const int &side,vector<int> &sides){
        if(index==nums.size())
            return sides[0]==sides[1]&&sides[1]==sides[2]&&sides[2]==sides[3];
        for(int i=0;i<4;++i){
            if(sides[i]+nums[index]<=side){
                sides[i]+=nums[index];
                if(DFS(nums,index+1,side,sides))
                    return true;
                sides[i]-=nums[index];
            }
        }
        return false;
    }
};
```