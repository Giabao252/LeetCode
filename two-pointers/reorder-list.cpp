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
    void reorderList(ListNode* head) {
        if (!head || !head->next) return; // Handle edge cases

        // Step 1: Find the middle of the list
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Step 2: Reverse the second half of the list
        ListNode* head2 = slow->next;
        slow->next = nullptr; // Split the list into two halves

        ListNode* prev = nullptr;
        ListNode* curr = head2;

        while (curr != nullptr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }

        head2 = prev; // Now head2 is the head of the reversed second half
        ListNode* tmp1 = head;
        ListNode* tmp2 = head2;

        while (head2 != nullptr) {
            tmp1 = head->next;
            tmp2 = head2->next;

            head->next = head2; // Link first node of the second half
            head2->next = tmp1; // Link back to the first half

            head = tmp1; // Move to the next node in the first half
            head2 = tmp2; // Move to the next node in the second half
        }
    }
};