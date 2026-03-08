


typedef struct {
    int *arr;
    int front;
    int rear;
    int size;
    int capacity;


    
} MyCircularDeque;


MyCircularDeque* myCircularDequeCreate(int k) {
    MyCircularDeque* obj = malloc(sizeof(MyCircularDeque));
    obj->arr = malloc(sizeof(int)*k);
    obj->front = 0;
    obj->rear = -1;
    obj->size = 0;
    obj->capacity = k; 

    return obj;

    
}


bool myCircularDequeInsertFront(MyCircularDeque* obj, int value) {
    if(obj->size==obj->capacity)
       return false;
    obj->front = (obj->front-1+obj->capacity)%obj->capacity;
    obj->arr[obj->front] = value;
    obj->size++;

    if(obj->size==1)
      obj->rear = obj->front;

    return true;
    
}

bool myCircularDequeInsertLast(MyCircularDeque* obj, int value) {
    if(obj->size==obj->capacity)
       return false;
    obj->rear = (obj->rear+1)%obj->capacity;
    obj->arr[obj->rear] = value;
    obj->size++;
 
    return true;

}

bool myCircularDequeDeleteFront(MyCircularDeque* obj) {
    if(obj->size==0)
      return false;
    obj->front = (obj->front + 1 )%obj->capacity;
    obj->size--;

    return true;
    
}

bool myCircularDequeDeleteLast(MyCircularDeque* obj) {
    if(obj->size==0)
      return false;
    obj->rear = (obj->rear - 1 + obj->capacity)%obj->capacity;
    obj->size--;

    return true;
    
}

int myCircularDequeGetFront(MyCircularDeque* obj) {
    if(obj->size==0)
       return -1;
    return obj->arr[obj->front];
    
}

int myCircularDequeGetRear(MyCircularDeque* obj) {
    if(obj->size==0)
       return -1;
    return obj->arr[obj->rear];
}

bool myCircularDequeIsEmpty(MyCircularDeque* obj) {
    return obj->size==0;
}

bool myCircularDequeIsFull(MyCircularDeque* obj) {
    return obj->size == obj->capacity;
}

void myCircularDequeFree(MyCircularDeque* obj) {
    free(obj->arr);
    free(obj);
}

/**
 * Your MyCircularDeque struct will be instantiated and called as such:
 * MyCircularDeque* obj = myCircularDequeCreate(k);
 * bool param_1 = myCircularDequeInsertFront(obj, value);
 
 * bool param_2 = myCircularDequeInsertLast(obj, value);
 
 * bool param_3 = myCircularDequeDeleteFront(obj);
 
 * bool param_4 = myCircularDequeDeleteLast(obj);
 
 * int param_5 = myCircularDequeGetFront(obj);
 
 * int param_6 = myCircularDequeGetRear(obj);
 
 * bool param_7 = myCircularDequeIsEmpty(obj);
 
 * bool param_8 = myCircularDequeIsFull(obj);
 
 * myCircularDequeFree(obj);
*/