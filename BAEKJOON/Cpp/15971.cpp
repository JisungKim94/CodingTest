#include <algorithm>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, start, finish;
    cin >> N >> start >> finish;
    if (start == finish) {
        cout << 0;
        return 0;
    }

    vector<vector<vector<int>>> graph(N + 1);
    for (int i = 0; i < N - 1; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }

    for (auto &conn : graph[start]) {
        if (conn[0] == finish) {
            cout << 0;
            return 0;
        }
    }

    priority_queue<vector<int>> heap;
    heap.push({0, start});
    vector<int> dist(N + 1, 2e9), parent(N + 1, -1), costs(N + 1, 0);
    dist[start] = 0;

    while (!heap.empty()) {
        auto ht = heap.top(); heap.pop();
        int cCost = -ht[0], cRoom = ht[1];
        if (cCost > dist[cRoom]) continue;

        // cout<<"cC: "<<cCost<<", cR: "<<cRoom<<endl;

        for (auto &conn : graph[cRoom]) {
            int nRoom = conn[0], edgeW = conn[1];
            int nCost = cCost + edgeW;
            if (dist[nRoom] > nCost) {
                dist[nRoom] = nCost;
                parent[nRoom] = cRoom;
                costs[nRoom] = edgeW;
                heap.push({-nCost, nRoom});
            }
        }
    }

    // for (int cur : parent) {
    //     cout<<cur<<" ";
    // }
    // cout<<endl;
    parent[start] = -1;
    // for (int cur = finish; cur != -1; cur = parent[cur]) {
    //     cout<<cur<<" ";
    // }
    // cout<<endl;

    int maxEdge = 0;
    for (int cur = finish; cur != start; cur = parent[cur]) {
        maxEdge = max(maxEdge, costs[cur]);
    }

    cout << (dist[finish] - maxEdge);
    return 0;
}
