/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode* first = headA;
    struct ListNode* secound = headB;
    while(first!=secound){
        if(first == NULL){
            first = headB;
        }
        else{
            first = first->next;
        }
        if(secound==NULL){
            secound = headA;
        }
        else{
            secound=secound->next;
        }

    }
    return first;
}    