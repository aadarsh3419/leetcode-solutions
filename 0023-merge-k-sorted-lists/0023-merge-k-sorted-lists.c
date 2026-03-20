/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* merge(struct ListNode* l1,struct ListNode* l2){
    if(l1==NULL)return l2;
    if(l2==NULL)return l1;
    if(l1->val < l2->val){
        l1->next = merge(l1->next,l2);
        return l1;
    }
    else{
        l2->next = merge(l1,l2->next);
        return l2;
    }

    

}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    if(listsSize == 0)return NULL;
    
    while(listsSize>1){
        int i =0, j = (listsSize-1);


        while(i<j){
        lists[i] = merge(lists[i],lists[j]);
        i++;
        j--;

    }

    listsSize = (listsSize + 1)/2;

    }
    return lists[0];
    
}