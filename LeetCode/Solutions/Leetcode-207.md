> 本题的实质是判断一个图有没有环

1. 拓扑排序
> 时间复杂度为O(N+M) 其中N为点的个数，M为边的个数，空间复杂度为O(N+M) 

```C++
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegrees(numCourses,0);
        queue<int> zero_indegrees;  // 入度为0的顶点序列
        vector<vector<int>> adjacents(numCourses,vector<int>());
        int num=numCourses;
        for(int i=0;i<prerequisites.size();++i){
            indegrees[prerequisites[i][0]]++;
            adjacents[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }
        for(int i=0;i<numCourses;++i){
            if(indegrees[i]==0){
                zero_indegrees.push(i);
                --num;
            }
        }
        while(!zero_indegrees.empty()){
            int temp=zero_indegrees.front();
            zero_indegrees.pop();
            for(int i=0;i<adjacents[temp].size();++i){
                if(--indegrees[adjacents[temp][i]]==0){
                    zero_indegrees.push(adjacents[temp][i]);
                    --num;
                }
            }
        }
        return num==0;
    }
};
```

2. DFS 
> visited要记录三个状态：
> - 0 未被DFS访问
> - -1 已被其他结点的DFS访问
> - 1 已被当前结点的DFS访问
> visited[i]==-1 说明有其他结点访问过当前结点，是可以被拓扑消除的，无须继续访问  
> visited[i]===1 说明已被当前结点第二次访问

```C++
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjacents(numCourses,vector<int>());
        for(int i=0;i<prerequisites.size();++i){
            adjacents[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }
        for(int i=0;i<numCourses;++i){
            vector<int> visited(numCourses,0);
            if(!DFS(adjacents,visited,i))
                return false;
        }
        return true;
    }
private:
    bool DFS(vector<vector<int>> &adjacents,vector<int> &visited, int i){
        if(visited[i]==-1)  return true;
        if(visited[i]==1)   return false;
        visited[i]=1;
        for(auto it : adjacents[i]){
            if(!DFS(adjacents,visited,it))  return false;
        }
        visited[i]=-1;
        return true;
    }
};
```