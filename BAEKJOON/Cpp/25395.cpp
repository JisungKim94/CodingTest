#include <algorithm>
#include <vector>
#include <iostream>
#include <queue>
#include <set>
using namespace std;

int N, S;
vector<int> X, H;
vector<bool> visited;
vector<int> curr;
set<vector<int>> combos;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, S;
    cin >> N >> S;
    --S;  // indexing

    vector<int> X(N), H(N);
    for (int i = 0; i < N; i++) cin >> X[i];
    for (int i = 0; i < N; i++) cin >> H[i];

    set<int> unvisited;
    for (int i = 0; i < N; i++) 
        unvisited.insert(i);

    vector<int> answer;
    queue<int> q;

    q.push(S);
    unvisited.erase(S);
    answer.push_back(S);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        int L = X[u] - H[u];
        int R = X[u] + H[u];

        int lIdx = int(lower_bound(X.begin(), X.end(), L) - X.begin());

        for (auto it = unvisited.lower_bound(lIdx);
             it != unvisited.end() && X[*it] <= R; ) {
            int v = *it;
            q.push(v);
            answer.push_back(v);
            it = unvisited.erase(it);
        }
    }

    sort(answer.begin(), answer.end());
    for (int idx : answer) {
        cout << (idx + 1) << " ";
    }
    cout << "\n";
    return 0;
}
