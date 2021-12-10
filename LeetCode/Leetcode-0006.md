1. 模拟法
> 遍历每一个字符将其加入合适的行，可以用当前行和当前方向两个变量描述当前状态

```C++
class Solution {
public:
    string convert(string s, int numRows) {
        if(s.empty()||s.size()==1||numRows==1)  return s;
        int len=s.size();
        vector<string> rows(min(numRows,len));
        int curr_row=0;
        bool go_down=false;
        for(char c : s){
            rows[curr_row]+=c;
            if(curr_row==0||curr_row==numRows-1){
                go_down=!go_down;
            }
            curr_row+=go_down?1:-1;
        }
        string ans;
        for(string &row : rows) ans+=row;
        return ans;
    }
};
```