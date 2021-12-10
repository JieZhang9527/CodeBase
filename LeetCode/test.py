import os

path=r"/Users/zhangjie/GitHub/CodeBase/LeetCode"
for file in os.listdir(path):
    if(file.split('.')[-1]=='md'):
        temp=file.split('-')[-1].split('.')[0]
        prefix=""
        for i in range(4-len(temp)):
            prefix+="0"
        temp=prefix+temp
        name=file.split('-')[0]+'-'+temp+".md"
        print(file," ",name)
        os.rename("./"+file,"./"+name)
