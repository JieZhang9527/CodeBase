> 添加一个前导'.',使得开头的处理和其他部分相同
```C++
class Solution {
public:
    int compareVersion(string version1, string version2) {
        // 使第一级的处理和其他级相同
        version1.insert(version1.begin(),'.');
        version2.insert(version2.begin(),'.');
        int index1=0, index2=0;
        while(index1<version1.size()||index2<version2.size()){
            if(index1==version1.size()){
                while(index2<version2.size()){
                    if(strToInt(version2,index2)!=0)    return -1;
                }
                return 0;
            }
            else if(index2==version2.size()){
                while(index1<version1.size()){
                    if(strToInt(version1,index1)!=0)    return 1;
                }
                return 0;
            }
            else{
                int a=strToInt(version1,index1);
                int b=strToInt(version2,index2);
                if(a>b) return 1;
                else if(a<b)    return -1; 
            }
        }
        return 0;
    }
private:
    int strToInt(string &version, int &index){
        ++index;    // !!!
        string temp=string();
        while(index<version.size()&&version[index]!='.'){
            if(temp.empty()&&version[index]=='0')   ++index;
            else    temp+=version[index++];
        }
        int ans=0;
        for(int i=0;i<temp.size();++i){
            ans=ans*10+(temp[i]-'0');
        }
        return ans;
    }
};
```