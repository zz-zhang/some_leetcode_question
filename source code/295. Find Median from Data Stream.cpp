//
// Created by zizheng zhang on 2019-08-22.
//

#include <queue>
#include <vector>

class MedianFinder {
public:
    std::priority_queue<int> smaller;
    std::priority_queue<int, std::vector<int>, std::greater<int> > larger;
    double median;
    /** initialize your data structure here. */
    MedianFinder() {
        median = 0.0;
    }

    void addNum(int num) {
        if (num > median){
            larger.push(num);
        }
        else{
            smaller.push(num);
        }

        if (smaller.size() - larger.size() == 2){
            larger.push(smaller.top());
            smaller.pop();
        }
        else if (larger.size() > smaller.size()){
            smaller.push(larger.top());
            larger.pop();
        }

        if (smaller.size() == larger.size()){
            median = (double(smaller.top()) + double(larger.top())) / 2;
        }
        else{
            median = double(smaller.top());
        }
    }

    double findMedian() {
        return median;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */