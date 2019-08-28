//
// Created by zizheng zhang on 2019-08-28.
//

#include <string>
#include <queue>
#include <map>

class Solution {
public:
    bool allIn(std::map<char, int> counter, std::map<char, int> recorder){
        for (auto iter = counter.begin(); iter != counter.end(); ++iter){
            if (counter[iter->first] > recorder[iter->first]){
                return false;
            }
        }
        return true;
    }
    std::string minWindow(std::string s, std::string t) {
        std::string result(s);
        std::string subRes = "";
//        std::queue<char> q;
        std::map<char, int> recorder;
        std::map<char, int> counter;
        for (auto iter = t.begin(); iter != t.end(); ++iter){
            recorder[(*iter)] = 0;
            if (counter.find(*iter) == counter.end()){
                counter[(*iter)] = 1;
            }
            else{
                counter[(*iter)]++;
            }
        }

        for (auto iter = s.begin(); iter != s.end(); ++iter){
//            q.push(*iter);
            subRes += *iter;
            if (t.find(*iter) != std::string::npos){
                recorder[(*iter)]++;
                if (allIn(counter, recorder)){
                    result = (result.size() < subRes.size()) ? result : subRes;

                    recorder[subRes[0]] --;
                    subRes.erase(0, 1);
                    while ((!subRes.empty()) && (t.find(subRes[0]) == std::string::npos)){
                        subRes.erase(0, 1);
                    }
                    if (allIn(counter, recorder)){
                        result = (result.size() < subRes.size()) ? result : subRes;
                    }
                }

            }

        }
        return result;
    }
};