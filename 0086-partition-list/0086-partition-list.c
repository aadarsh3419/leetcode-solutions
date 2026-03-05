/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* partition(struct ListNode* head, int x) {
    struct ListNode smalldummy;
    struct ListNode bigdummy;
    struct ListNode* small = &smalldummy;
    struct ListNode* big = &bigdummy;
    small->next=NULL;
    big->next=NULL;
    while(head!=NULL){
        if(head->val<x){
            small->next = head;
            small = small->next;
        }
        else{
          big->next=head;
          big=big->next;
        }
        head = head->next;
    }
    big->next = NULL;
    small->next = bigdummy.next;
    return smalldummy.next;
}