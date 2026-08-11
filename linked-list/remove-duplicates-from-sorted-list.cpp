/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) {
            return head;
        }
        ListNode* new_head = new ListNode;
        new_head->val = head->val;
        new_head->next = nullptr;
        ListNode* new_ptr = new_head;

        ListNode* ptr1 = head;
        ListNode* ptr2 = ptr1->next;

        while (ptr2 != nullptr) {
            if (ptr1->val != ptr2->val) {
                new_ptr->next = new ListNode;
                new_ptr->next->val = ptr2->val;
                new_ptr = new_ptr->next;
                new_ptr->next = nullptr;
            }
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }

        return new_head;
        
    }
};