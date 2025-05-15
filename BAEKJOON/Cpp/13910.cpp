#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <cmath>
#include <set>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, s;
    vector<int> temp;
    cin >> N >> M;
    for (int i=0; i<M; i++) {
        cin >> s;
        temp.push_back(s);
    }
    
    set<int> S;
    for (int i = 0; i<M; i++) {
        S.insert(temp[i]);
        for (int j = 0; j<M; j++) {
            if (i!=j) S.insert(temp[i]+temp[j]);
        }        
    }
    // for (auto s:S) {
    //     cout<<s<<", ";
    // }
    // cout<<endl;

    vector<int> dp(N+1,999999);
    for (auto s : S) {
        int cnt = 0;
        for (int i = 0; i<N+1; i+=s) {
            dp[i] = min(cnt,dp[i]);
            cnt+=1;
        }
    }

    for (int i = 0; i<N+1; i++) {
        for (int j = 0; j<N+1; j++) {
            if (i+j >= N+1) {
                break;
            }
            if (i==j) continue;

            dp[i+j] = min(dp[i+j],dp[i]+dp[j]);
        }
    }

    // for (auto d:dp) {
    //     cout<<d<<", ";
    // }
    // cout<<endl;
    if (dp[N] == 999999) {
        cout<<-1;
    } else {
        cout<<dp[N];
    }
    return 0;
}
