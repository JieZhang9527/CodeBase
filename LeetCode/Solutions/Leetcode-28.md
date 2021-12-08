1. KMP
> KMP算法的核心的是计算出next数组，对于模式串的某一位置j，next[j]的值是该模式串从下标[0,j-1]的子串中，前缀和后缀相等的最大长度。具体实现方式：

```C++
class Solution {
public:
    int strStr(string haystack, string needle) {
        return KMP(haystack,needle,0);
    }
private:
    int KMP(string &str, string &pattern, int pos){
        if(pattern.empty()) return pos;
        vector<int> next(pattern.size(),0);
        getNext(pattern,next);
        int i=0, j=0;
        while(i<str.size()){
            if(j==-1||str[i]==pattern[j]){
                ++i;
                ++j;
            }
            else    j=next[j];
            if(j==pattern.size())   return i-pattern.size();  
        }
        return -1;
    }
    void getNext(string &pattern, vector<int> &next){
        next[0]=-1;
        int j=0, k=-1;
        while(j<pattern.size()-1){
            if(k==-1||pattern[j]==pattern[k]){
                ++j;
                ++k;
                next[j]=k;
            }
            else    k=next[k];
        }
    }
};
```