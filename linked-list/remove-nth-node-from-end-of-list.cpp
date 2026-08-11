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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy_node = new ListNode;
        dummy_node->val = 0;
        dummy_node->next = head;
        ListNode* ptr1 = dummy_node;
        ListNode* ptr2 = ptr1;

        while (n != 0) {
            ptr2 = ptr2->next;
            n--;
        }

        while (ptr2->next != nullptr) {
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }

        if (ptr1 == dummy_node) {
            return head->next;
        }

        ptr1->next = ptr1->next->next;
        
        return head;
    }
};