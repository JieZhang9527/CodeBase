1. 拓扑排序

```C++
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> ans;
        vector<int> indegrees(numCourses,0);
        queue<int> zero_indgrees;
        vector<vector<int>> adjacents(numCourses,vector<int>());
        for(int i=0;i<prerequisites.size();++i){
            indegrees[prerequisites[i][0]]++;
            adjacents[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }
        for(int i=0;i<numCourses;++i){
            if(indegrees[i]==0)
                zero_indgrees.push(i);
        }
        while(!zero_indgrees.empty()){
            int temp=zero_indgrees.front();
            zero_indgrees.pop();
            ans.push_back(temp);
            for(auto it : adjacents[temp]){
                if(--indegrees[it]==0)  
                    zero_indgrees.push(it);
            }
        }
        return (ans.size()==numCourses)?ans:vector<int>();
    }
};
```