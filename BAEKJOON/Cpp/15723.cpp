#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    std::unordered_map<std::string, std::string> premise;
    for (int i = 0; i < n; i++) {
        string str1, str2, str3;
        cin >> str1 >> str2 >> str3;
        premise[str1] = {str3};
    }

    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        string cur, temp, target, next;
        cin >> cur >> temp >> target;
        while (1) {
            if (premise[cur] == target) {
                cout<<"T"<<endl;
                break;
            }
            if (auto search = premise.find(premise[cur]); search == premise.end()) {
                cout<<"F"<<endl;
                break;
            }
            cur = premise[cur];
        }
    }
    return 0;
}
