/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    struct ListNode *fast,*slow;
    if(head==NULL|| head->next==NULL)
        return true;
    fast = head;
    slow = head;
    
    while(fast!=NULL&&fast->next!=NULL){
        slow = slow->next;
        fast = fast->next->next;
        }
    struct ListNode *prev = NULL;
    struct ListNode *current = slow;
    while(current!=NULL){
        struct ListNode *next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    struct ListNode *first = head;
    struct ListNode *secound = prev;
    while(secound!=NULL){
        if(first->val!=secound->val) 
            return false;
        first = first->next;
        secound = secound->next;
    } 
     
    return true;
}