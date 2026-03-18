/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* divide(struct ListNode* head){
    struct ListNode* slow = head;
    struct ListNode* fast = head->next;
    while(fast!=NULL&&fast->next!=NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    
    return slow;
}
struct ListNode* merge(struct ListNode* l1,struct ListNode* l2){
   struct ListNode dummy;
   struct ListNode* tail = &dummy;
   dummy.next = NULL;

   while(l1!=NULL&&l2!=NULL){
    if(l1->val<l2->val){
        tail->next = l1;
        l1 = l1->next;
    }
    else{
        tail->next = l2;
        l2 = l2->next;
    }
    tail = tail->next;
   }
   if(l1)tail->next = l1;
   if(l2)tail->next = l2;
   return dummy.next;
}
struct ListNode* sortList(struct ListNode* head) {
    if(head==NULL||head->next==NULL){
        return head;
    }
    struct ListNode* mid = divide(head);
    struct ListNode* right = mid->next;
    mid->next = NULL;
    struct ListNode* left = head;

    left = sortList(left);
    right = sortList(right);

    return merge(left,right);
}