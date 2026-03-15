/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* current = head;
    struct ListNode* prev = NULL;
    while(current!=NULL){
        struct ListNode* next = current->next;
        current->next=prev;
        prev = current;
        current =next;
    }
    return prev;
} 