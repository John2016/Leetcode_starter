/**
 * 2019/9/10
 * 将2个以链表形式存储的数字相加并得到链表
 * 要点是链表结构的操作，指针与引用的使用
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        int xx = 0, yy = 0, carry = 0, sum = 0;
        ListNode *h = NULL, **t = &h;

        while (l1 != NULL || l2 != NULL)
        {
            xx = get_and_move(l1);
            yy = get_and_move(l2);

            sum = carry + xx + yy;

            ListNode *node = new ListNode(sum%10);
            *t = node;
            t = (&node->next);

            carry = sum/10;
        }

        if (carry > 0)
        {
            ListNode *node = new ListNode(carry%10);
            *t = node;
        }

        return h;
    }

private:
    int get_and_move(ListNode* &l)
    {
        int x = 0;
        if (l != NULL)
        {
            x = l->val;
            l = l->next;
        }
    return x;
    }
};