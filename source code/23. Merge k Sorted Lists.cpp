//
// Created by zizheng zhang on 2019-08-28.
//
#include <queue>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
        for (auto iter = lists.begin(); iter != lists.end(); ++iter){
            while (*iter != NULL){
                pq.push((*iter)->val);
                *iter = (*iter)->next;
            }
        }
        ListNode* head = new ListNode(-1);
        ListNode* node = head;
        while (!pq.empty()){
            node->next = new ListNode(pq.top());
            node = node->next;
            pq.pop();
        }
        return head->next;
    }
};