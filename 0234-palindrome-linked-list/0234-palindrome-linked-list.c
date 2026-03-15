/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverse(struct ListNode* head){
    struct ListNode* prev = NULL;
    struct ListNode* current = head;
    while(current){
        struct ListNode* next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}
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
    slow = reverse(slow);
    struct ListNode* current = head;
    while(slow){
        
        if(current->val!=slow->val){
            return false;
        }
        slow = slow->next;
        current = current->next;

    }
    return true;

}
