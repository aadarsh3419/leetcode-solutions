


typedef struct {
    int size;
    int top;
    int *arr;
    
} MinStack;


MinStack* minStackCreate() {
    MinStack* s = malloc(sizeof(MinStack));
    s->top = -1;
    s->size = 10; 
    s->arr = (int*)malloc (s->size * sizeof(int));

    return s;
}

void minStackPush(MinStack* obj, int val) {
    if(obj->top == obj->size-1){
        obj->size = obj->size*2;
        obj->arr = realloc(obj->arr,obj->size*sizeof(int));
    }
       
    obj->top++;
    obj->arr[obj->top] = val; 
    
    
} 

void minStackPop(MinStack* obj) {
    if(obj->top == -1)
       return;
    obj->top--;
    
}

int minStackTop(MinStack* obj) {
    if(obj->top == -1)
       return-1;
    return obj->arr[obj->top];
    
}

int minStackGetMin(MinStack* obj) {
    if(obj->top == -1)
        return-1;
    int mini = obj->arr[0];
    for(int i=0;i<=obj->top;i++){
        if(obj->arr[i] < mini)
            mini=obj->arr[i];
    }
    return mini;
    
}

void minStackFree(MinStack* obj) {
    
    free(obj->arr);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/