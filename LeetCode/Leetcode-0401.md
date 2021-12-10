1. 位运算

> Brian Kernighan算法(布莱恩·柯林翰 算法)：n & (n-1)  则n的二进制串中最右边的1将变为0

```C++
class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> ans;
        for(int i=0;i<12;++i){
            for(int j=0;j<60;++j){
                if(count(i)+count(j)==num){
                    string temp=string();
                    temp+=to_string(i)+":";
                    if(j<10)    temp+="0";
                    temp+=to_string(j);
                    ans.push_back(temp);
                }
            }
        }
        return ans;
    }
    int count(int num){
        int ans=0;
        while(num){
            num &= (num-1);
            ++ans;
        }
        return ans;
    }
};
```