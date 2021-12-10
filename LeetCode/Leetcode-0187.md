1. 遍历
> 注意特殊判断，否则i=0时会报错

```C++
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> ans;
        if(s.size()<10) return ans;
        unordered_set<string> ust, temp;
        for(int i=0;i<=s.size()-10;++i){
            cout<<"!!"<<endl;
            string str=s.substr(i,10);
            if(ust.find(str)!=ust.end())    temp.insert(str);
            else    ust.insert(str);
        }
        for(string str : temp) ans.push_back(str);
        return ans;
    }
};
```

2. 位运算
> 使用位操作优化上面的第一种解法  
> 解法1中获取长度为10的子串使用:string key = s.substr(i,10),但是在递增的过程中,z子串相对于前一个子串只是少了开头一个字母,多了末尾一个字母,剩下的九个字母没有变化-> 将字符串编码为数字序列,通过移位操作保留之前的信息

 
> 解决方案:  
A -> 00   C -> 01   G -> 10   T -> 11   通过这个对应关系将字符串映射为二进制序列每遍历到一个新字母,将原来的二进制序列key左移两位,然后加上新加入字母对应的二进制序列
10个字母只需要20位二进制序列,因此key与1111 1111 1111 1111 1111(0xfffff) 与运算将高位截断,只保留低二十位


```C++
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<int,int> mp;
        mp['A'-'A']=0;
        mp['C'-'A']=1;
        mp['G'-'A']=2;
        mp['T'-'A']=3;
        int key=0;
        //第一组单独初始化
        for(int i=0;i<10;++i)   key = key << 2 | mp[s[i]-'A'];
        unordered_set<int> st;      //记录已经出现的序列
        unordered_set<string> temp; //记录目标子串,避免重复
        st.insert(key);
        for(int i=10;i<s.size();++i){
            key = key << 2 | mp[s[i]-'A'];
            key &= 0xfffff;         //保留二十位
            if(st.find(key)!=st.end())  temp.insert(s.substr(i-9,10));
            else    st.insert(key);
        }
        vector<string> ans;
        for(string str : temp)  ans.push_back(str);
        return ans;
    }
};
```