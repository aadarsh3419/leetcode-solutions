/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverse(struct ListNode* head){
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    while(curr!=NULL){
        struct ListNode* next = curr->next;
        curr->next = prev;
        prev= curr;
        curr = next;
    }
    return prev;
}
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode dummy;
    dummy.next = head;

    struct ListNode* p = &dummy;
    while(true){
        struct ListNode* c = p;
        for(int i=0; i<k; i++){
            c = c->next;
            if(c == NULL){
                return dummy.next;
            }
        }
       
        struct ListNode* start = p->next;
        struct ListNode* nextgroup = c->next;

        struct ListNode* prev = nextgroup;
        struct ListNode* curr = start;

        while(curr!=nextgroup){
            struct ListNode* temp =curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        p->next = c;
        p = start;

        
        
    }
    
    
   
    
}