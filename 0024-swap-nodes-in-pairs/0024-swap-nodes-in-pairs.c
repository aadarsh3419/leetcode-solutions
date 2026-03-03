/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    if(head==NULL || head->next ==NULL)
       return head;
    
    struct ListNode dummy;
    dummy.next=head;

    struct ListNode* prev = &dummy;

    while(prev->next!=NULL&& prev->next->next != NULL){
        struct ListNode* first = prev->next;
        struct ListNode* secound = first->next;
        
        first->next = secound->next;
        secound->next = first;
        prev->next=secound;
        prev = first;
    }
    return dummy.next;
}