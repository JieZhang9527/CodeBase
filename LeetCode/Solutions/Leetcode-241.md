1. 递归
> 每次将表达式分为两个部分，分别计算

```C++
class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        if(expression.empty())  return {0};
        vector<int> ans;
        int index=0;
        int num=0;
        while(index<expression.size()&&!isOperation(expression[index])){
            num=num*10+(expression[index]-'0');
            ++index;
        }
        if(index==expression.size()){
            ans.push_back(num);
            return ans;
        }
        for(int i=0;i<expression.size();++i){
            if(isOperation(expression[i])){
                auto ans1=diffWaysToCompute(expression.substr(0,i));
                auto ans2=diffWaysToCompute(expression.substr(i+1));
                for(int p=0;p<ans1.size();++p){
                    for(int q=0;q<ans2.size();++q){
                        ans.push_back(caculate(ans1[p],expression[i],ans2[q]));
                    }
                }
            }
        }
        return ans;
    }
private:
    bool isOperation(char c){
        return c=='+'||c=='-'||c=='*';
    }
    int caculate(int num1, char c, int num2){
        switch(c){
            case '+':
                return num1+num2;
            case '-':
                return num1-num2;
            case '*':
                return num1*num2;
        }
        return -1;
    }
};
```
2. 递归优化

> 将重复计算记录下来

```C++
class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        if(expression.empty())  return {0};
        if(ump.find(expression)!=ump.end()) return ump[expression];
        vector<int> ans;
        int index=0;
        int num=0;
        while(index<expression.size()&&!isOperation(expression[index])){
            num=num*10+(expression[index]-'0');
            ++index;
        }
        if(index==expression.size()){
            ans.push_back(num);
            ump[expression]=ans;
            return ans;
        }
        for(int i=0;i<expression.size();++i){
            if(isOperation(expression[i])){
                auto ans1=diffWaysToCompute(expression.substr(0,i));
                auto ans2=diffWaysToCompute(expression.substr(i+1));
                for(int p=0;p<ans1.size();++p){
                    for(int q=0;q<ans2.size();++q){
                        ans.push_back(caculate(ans1[p],expression[i],ans2[q]));
                    }
                }
            }
        }
        ump[expression]=ans;
        return ans;
    }
private:
    unordered_map<string,vector<int>> ump;
    bool isOperation(char c){
        return c=='+'||c=='-'||c=='*';
    }
    int caculate(int num1, char c, int num2){
        switch(c){
            case '+':
                return num1+num2;
            case '-':
                return num1-num2;
            case '*':
                return num1*num2;
        }
        return -1;
    }
};
```