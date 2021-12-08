1. 辅助队列

```C++
class MyStack {
public:
    /** Initialize your data structure here. */
    queue<int> q, help;
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        q.push(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        if(q.empty())   return -1;
        while(q.size()!=1){
            help.push(q.front());
            q.pop();
        }
        int ans=q.front();
        q.pop();
        while(!help.empty()){
            q.push(help.front());
            help.pop();
        }
        return ans;
    }
    
    /** Get the top element. */
    int top() {
        if(q.empty())   return -1;
        while(q.size()!=1){
            help.push(q.front());
            q.pop();
        }
        int ans=q.front();
        help.push(q.front());
        q.pop();
        while(!help.empty()){
            q.push(help.front());
            help.pop();
        }
        return ans;
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q.empty();
    }
};
```