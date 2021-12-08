1. 递归

> 初始化：每种物品单独购买，不使用大礼包  
> 对于每种大礼包，递归的求解购买清单减去当前大礼包的购买清单的最少购买价格

```C++
class Solution {
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        int ans=0;
        for(int i=0;i<price.size();++i) ans+=price[i]*needs[i];
        for(int i=0;i<special.size();++i){
            vector<int> clone=needs;
            int j=0;
            for(;j<clone.size();++j){
                clone[j]=clone[j]-special[i][j];
                if(clone[j]<0)  break;
            }
            if(j==clone.size())
                ans=min(ans,special[i][j]+shoppingOffers(price,special,clone));
        }
        return ans;
    }
};   
```

1. 记忆化搜索

> 用一个map记录已经求过的购买清单的最低价格，避免重复计算

```C++
class Solution {
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        map<vector<int>,int> mp;
        return helper(price,special,needs,mp);
    }
    int helper(vector<int>& price, vector<vector<int>>& special, vector<int>& needs,map<vector<int>,int> &mp){
        int ans=0;
        for(int i=0;i<price.size();++i) ans+=price[i]*needs[i];
        for(int i=0;i<special.size();++i){
            vector<int> clone=needs;
            int j=0;
            for(;j<clone.size();++j){
                clone[j]=clone[j]-special[i][j];
                if(clone[j]<0)  break;
            }
            if(j==clone.size()){
                if(mp.find(clone)!=mp.end())    ans=min(ans,special[i][j]+mp[clone]);
                else{
                    ans=min(ans,special[i][j]+helper(price,special,clone,mp));
                    mp[clone]=ans;
                }
            }
        }
        return ans;
    }
};
```