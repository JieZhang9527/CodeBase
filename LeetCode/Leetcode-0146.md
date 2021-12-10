1. 哈希表+双向链表
> 双向链表按照被使用的顺序存储这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。  
哈希表通过缓存数据的键映射到其在双向链表中的位置。

```C++
struct DLinkedNode{
    int key,value;
    DLinkedNode *prev, *next;
    DLinkedNode(): key(0), value(0) {}
    DLinkedNode(int _key,int _value): key(_key), value(_value) {}
};
class LRUCache {
public:
    LRUCache(int _capacity): capacity(_capacity), size(0) {
        head=new DLinkedNode();
        tail=new DLinkedNode();
        head->next=tail;
        tail->prev=head;
    }

    int get(int key) {
        if(cache.find(key)==cache.end())    return -1;
        DLinkedNode *temp=cache[key];
        moveToHead(temp);
        return temp->value;
    }
    
    void put(int key, int value) {
        if(cache.find(key)!=cache.end()){
            DLinkedNode *temp=cache[key];
            temp->value=value;
            moveToHead(temp);
        }
        else{
            DLinkedNode *temp=new DLinkedNode(key,value);
            cache[key]=temp;
            addToHead(temp);
            ++size;
            if(size>capacity){
                DLinkedNode *removed=removeTail();
                cache.erase(removed->key);
                delete(removed);
                --size;
            }
        }
    }
private:
    unordered_map<int,DLinkedNode*> cache;
    DLinkedNode *head, *tail;
    int size, capacity;
    void addToHead(DLinkedNode *node){
        node->next=head->next;
        node->prev=head;
        head->next->prev=node;
        head->next=node;
    }
    void removeNode(DLinkedNode *node){
        node->prev->next=node->next;
        node->next->prev=node->prev;
    }
    void moveToHead(DLinkedNode *node){
        removeNode(node);
        addToHead(node);
    }
    DLinkedNode *removeTail(){
        DLinkedNode *temp=tail->prev;
        removeNode(temp);
        return temp;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
 ```