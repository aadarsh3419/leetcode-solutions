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
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    

    struct ListNode dummy;
    dummy.next = NULL;
    struct ListNode* curr = &dummy;
    struct ListNode* tl1 = reverseList(l1);
    struct ListNode* tl2 =reverseList(l2);
    
    int carry = 0;
    
    while(tl1!=NULL||tl2!=NULL||carry){
        int sum = carry;
        
        if(tl1!=NULL){
            sum+=tl1->val;
            tl1 = tl1->next;
        }
        if(tl2!=NULL){
            sum+=tl2->val;
            tl2 = tl2->next;
        }
        carry = sum/10;

        struct ListNode* node = malloc(sizeof(struct ListNode));
        node->val = sum%10;
        node->next = NULL;

        curr->next = node;
        curr = curr->next;
        
    }
    
    return reverseList(dummy.next);

    
}