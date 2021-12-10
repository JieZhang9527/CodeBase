1. 回溯

```C++
class Solution {
public:
    bool isAdditiveNumber(string num) {
        int index1=0;
        for(int index2=index1+1;index2<num.size();++index2){
            for(int index3=index2+1;index3<num.size();++index3){
                if(DFS(num,index1,index2,index3)) return true;
            }
        }
        return false;
    }
private:
    string strAdd(string &str1, string &str2){
        string ans=string();
        int index1=str1.size()-1, index2=str2.size()-1;
        int carry=0;
        while(index1>=0||index2>=0){
            int a=index1>=0?str1[index1]-'0':0;
            int b=index2>=0?str2[index2]-'0':0;
            int sum=a+b+carry;
            ans=to_string(sum%10)+ans;
            carry=sum/10;
            --index1;   --index2;
        }
        if(carry)   ans=to_string(carry)+ans;
        return ans;
    }
    // index1 index2 index3 分别代表第一第二第三个数字的起始位置
    bool DFS(string &s, int index1, int index2, int index3){
        if((s[index1]=='0'&&index2-index1>1)||(s[index2]=='0'&&index3-index2>1)) return false;
        string str1=s.substr(index1,index2-index1);
        string str2=s.substr(index2,index3-index2);
        string str=strAdd(str1,str2);
        if(index3+str.size()>s.size()||str!=s.substr(index3,str.size()))    return false;
        if(index3+str.size()==s.size()) return true;
        return DFS(s,index2,index3,index3+str.size());
    }
};
```