/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void reorderList(struct ListNode* head) {
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    struct ListNode* p = head;
    while(fast!=NULL&&fast->next!=NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    struct ListNode* secound = slow->next;
    slow->next = NULL;

    struct ListNode* prev = NULL;
    while(secound){
        struct ListNode* next = secound->next;
        secound->next = prev;
        prev = secound;
        secound = next;
    }

    struct ListNode* first = head;
    secound = prev;
    while(secound){
        struct ListNode* t1 = first->next;
        struct ListNode* t2 = secound->next;
        first->next = secound;
        secound->next = t1;
        first = t1;
        secound = t2;
    }
    
    
}