1. 辅助栈
> 使用help单调递减栈

```C++
class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> data;
    stack<int> help;    //单调递减栈
    MinStack() {
        
    }
    
    void push(int x) {
        data.push(x);
        if(help.empty()||x<=help.top())
            help.push(x);
    }
    
    void pop() {
        if(data.top()==help.top())  help.pop();
        data.pop();
    }
    
    int top() {
        return data.top();
    }
    
    int getMin() {
        return help.top();
    }
};

```