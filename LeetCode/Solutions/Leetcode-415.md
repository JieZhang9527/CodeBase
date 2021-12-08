1. 遍历

```C++
class Solution {
public:
    string addStrings(string num1, string num2) {
        string ans;
        int i=num1.size()-1, j=num2.size()-1;
        int carry=0;
        while(i>=0||j>=0){
            int a=i>=0?num1[i]-'0':0;
            int b=j>=0?num2[j]-'0':0;
            int temp=carry+a+b;
            ans=to_string(temp%10)+ans;
            carry=temp/10;
            --i; --j;
        }
        if(carry)   ans=to_string(carry)+ans;
        return ans;
    }
};
```