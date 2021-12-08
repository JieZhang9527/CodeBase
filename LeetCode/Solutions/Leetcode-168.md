1. 10进制转26进制

```C++
class Solution {
public:
    string convertToTitle(int n) {
        string ans;
        while(n){
            int num=n%26;
            if(num==0){
                ans+='Z';
                n=n/26-1;
            }
            else{
                ans+=num-1+'A';
                n=n/26;
            }
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
```