/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if(head == NULL)
      return head;
    
    struct ListNode dummy;
    dummy.next = head;

    struct ListNode* prev = &dummy;
    while(1){
        struct ListNode* kth = prev;
        for(int i = 0; i < k; i++){
            kth = kth->next;
            if(kth==NULL)
               return dummy.next;
        }
        struct ListNode* current = prev->next;

        for(int j = 0; j < k-1; j++){ 
           struct ListNode* temp = current->next;
           current->next = temp->next;
           temp->next = prev->next; 
           prev->next = temp; 
        }
        prev = current;
         
    }
   
             
    
    return dummy.next;

    
}