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
    struct ListNode* nexte = NULL;
    while (current!=NULL){
        nexte = current->next;
        current->next = prev;
        prev = current;
        current = nexte;
    }
    return prev;
} 