1. 遍历
> 判断当前元素对应值是否大于下一个元素对应值，由此判断应该怎么加当前值

```C++
class Solution {
public:
    int romanToInt(string s) {
        int result=0;
        map<char,int> mp={{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
        for(int i=0;i<s.size();){
            if(i+1==s.size()){
                result+=mp[s[i]];
                break;
            }
            else{
                if(mp[s[i]]>=mp[s[i+1]]){
                    result+=mp[s[i]];
                    i++;
                }
                else{
                    result=result+(mp[s[i+1]]-mp[s[i]]);
                    i+=2;
                }
            }
        }
        return result;
    }
};
```