/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if(head==NULL||head->next==NULL){
        return head;}
    struct ListNode* p = head;
    int len = 1;
    
    
    while(p->next!=NULL){
        p = p->next;
        len++;

    }
    p->next = head;
    k = k % len; 
    int move = len-k;
    
    for(int i=0;i<move;i++){
        p = p->next;
    }
    struct ListNode* newhead = p->next;
    p->next = NULL;
    return newhead;
} 