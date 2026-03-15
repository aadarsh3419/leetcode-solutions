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

    struct ListNode* curr = &dummy;

    while(curr->next!=NULL&&curr->next->next!=NULL){
        struct ListNode* first = curr->next;
        struct ListNode* secound = first->next;

        first->next = secound->next;
        secound->next = first;
        curr->next = secound;

        curr=first;

    }
    return dummy.next;
}