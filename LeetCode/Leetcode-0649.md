1. 贪心算法

> 每个字母总是尽量去淘汰对方

```C++
class Solution {
public:
    string predictPartyVictory(string senate) {
        //判断当前序列中还有没有对应字母,如果没有,则可判断哪方胜出
        bool R=true,D=true;
        //每次遍历到一个字母,不立即去找后边的另一个字母,而是先记录下来
        //person>0 R有权利淘汰D
        //person<0 D有权利淘汰R
        int person=0;
        while(R&&D){
            R=false;D=false;
            for(int i=0;i<senate.size();++i){
                if(senate[i]=='R'){
                    R=true;
                    if(person<0)    senate[i]='#';
                    ++person; 
                }
                else if(senate[i]=='D'){
                    D=true;
                    if(person>0)    senate[i]='#';
                    --person;
                }
            }
        }
        return D?"Dire":"Radiant";
    }
};
```