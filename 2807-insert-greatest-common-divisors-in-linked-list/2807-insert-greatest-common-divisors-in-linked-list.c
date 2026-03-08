/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 int gcd(int a,int b){
    while(b!=0){
        int t = b;
        b =a%b;
        a = t;

    }
    return a;
 }
struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) 
{ 
    struct ListNode* temp = head;
    while(temp->next!=NULL)
    {
        int g = gcd(temp->val,temp->next->val);
        struct ListNode* newnode = malloc(sizeof(struct ListNode));
        newnode->val = g;

        newnode->next = temp->next;
        temp->next = newnode;

        temp = newnode->next;
    }
    return head;

 
    
}