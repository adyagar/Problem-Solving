/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode * B = headB;
        while (headA!=NULL)
        {
            //cout<<headA->val<<endl;
            headB = B;
            while (headB!=NULL)
            {//cout<<"ho"<<headB->val<<endl;
                
            
            if (headA->next == headB || headA == headB)
            {
                return headB;
            }
                            headB= headB->next;

            }
            headA = headA->next;
        }
        
        
        return NULL;
        
    }
};