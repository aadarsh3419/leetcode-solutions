/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode dummy;
    dummy.next=head;
    struct ListNode *fast ,*slow; 
    slow =&dummy;
    fast = &dummy;
    for(int i=0;i<=n;i++){
        fast = fast->next;
    }
    while(fast!=NULL){
        fast = fast->next;
        slow = slow->next;
        
    }
    slow->next = slow->next->next;
    return dummy.next;
    
}