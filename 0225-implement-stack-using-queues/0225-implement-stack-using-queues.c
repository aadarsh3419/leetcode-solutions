


typedef struct {
    int top;
    int size;
    int *arr;
    
} MyStack;


MyStack* myStackCreate() {
    
   MyStack* s =(MyStack*) malloc(sizeof(MyStack));
    s->size = 100;
    s->top = -1;

    s->arr = (int*) malloc(s->size *sizeof(int));
    
    return s;
    
}

void myStackPush(MyStack* obj, int x) {
    obj->top++;
    obj->arr[obj->top] = x; 
    
}

int myStackPop(MyStack* obj) {
    if(obj->top == -1)
       return -1;
    int value = obj->arr[obj->top];
    obj->top--;
    return value;
    
}

int myStackTop(MyStack* obj) {
    if(obj->top == -1)
       return -1;
    return obj->arr[obj->top];
    
}

bool myStackEmpty(MyStack* obj) {
    return obj->top == -1;
    
}

void myStackFree(MyStack* obj) {
    free(obj->arr);
    free(obj);

    
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/
