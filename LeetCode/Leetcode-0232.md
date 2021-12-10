1. 辅助栈

```C++
class MyQueue {
public:
    /** Initialize your data structure here. */
    stack<int> st,help;
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        st.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(st.empty())  return -1;
        while(!st.empty()){
            help.push(st.top());
            st.pop();
        }
        int ans=help.top();
        help.pop();
        while(!help.empty()){
            st.push(help.top());
            help.pop();
        }
        return ans;
    }
    
    /** Get the front element. */
    int peek() {
        if(st.empty())  return -1;
        while(!st.empty()){
            help.push(st.top());
            st.pop();
        }
        int ans=help.top();
        while(!help.empty()){
            st.push(help.top());
            help.pop();
        }
        return ans;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return st.empty();
    }
};
```