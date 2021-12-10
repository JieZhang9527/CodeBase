1. 遍历处理
> 注意isdigit()头文件``<cctype>``和整型溢出判断条件

```C++
class Solution {
public:
    int myAtoi(string str) {
        if(str.empty()) return 0;
        int index=0, ans=0;
        while(index<str.size()){
            if(str[index]==' ') ++index;
            else break;
        }
        if(index==str.size())   return ans;
        bool flag=true;
        if(str[index]=='+'){
            flag=true;
            index++;
        } 
        else if(str[index]=='-'){
            flag=false;
            index++;
        }
        while(index<str.size()){
            if(!isdigit(str[index]))    break;
            int temp=str[index]-'0';
            if(ans>INT_MAX/10||(ans==INT_MAX/10&&temp>7)){
                return flag?INT_MAX:INT_MIN;
            }
            ans=ans*10+temp;
            ++index;
        }
        return flag?ans:-ans;
    }
};
```