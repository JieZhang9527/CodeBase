1. 双指针

```C++
class Solution {
public:
    string addBinary(string a, string b) {
        int index1=a.size()-1, index2=b.size()-1;
        string ans=string();
        int carry=0;
        while(index1>=0||index2>=0){
            int num1=index1>=0?a[index1]-'0':0;
            int num2=index2>=0?b[index2]-'0':0;
            int temp=num1+num2+carry;
            ans=to_string(temp%2)+ans;
            carry=temp/2;
            --index1;
            --index2;
        }
        if(carry)   ans=to_string(carry)+ans;
        return ans;
    }
};
```