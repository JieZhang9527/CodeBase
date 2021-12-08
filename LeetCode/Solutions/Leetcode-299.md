1. 哈希

```C++
class Solution {
public:
    string getHint(string secret, string guess) {
        string ans=string();
        int arrayA[10]={0}, arrayB[10]={0};
        int countA=0, countB=0;
        for(int i=0;i<secret.size();++i){
            if(secret[i]==guess[i]) ++countA;
            else{
                ++arrayA[secret[i]-'0'];
                ++arrayB[guess[i]-'0'];
            }
        }
        for(int i=0;i<10;i++){
            countB+=min(arrayA[i],arrayB[i]);
        }
        ans+=to_string(countA)+'A'+to_string(countB)+'B';
        return ans;
    }
};
```