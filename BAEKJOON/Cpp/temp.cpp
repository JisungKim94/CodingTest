#include <iostream>
#include <vector>
#include <limits>
#include <queue>
#include <unordered_map>

using namespace std;

const int INF = numeric_limits<int>::max();

int main() {
    ios::sync_with_stdio(false); // Speeds up IO
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<int> A(N);
    for (int& a : A) {
        cin >> a;
    }
    A.back() = 0;

    // Graph representation using an adjacency list
    unordered_map<int, vector<pair<int, int>>> graph;

    for (int i = 0; i < M; ++i) {
        int a, b, t;
        cin >> a >> b >> t;
        if (A[a] == 1 || A[b] == 1) {
            continue;
        }
        graph[a].push_back({b, t});
        graph[b].push_back({a, t});
    }

    // Dijkstra's algorithm
    vector<int> dist(N, INF);
    dist[0] = 0;
    queue<pair<int, int>> que;
    que.push({0, 0}); // Pair of (cost, node)

    while (!que.empty()) {
        auto [ccost, cnode] = que.front();
        que.pop();

        if (ccost > dist[cnode] || cnode == N - 1) {
            continue;
        }

        for (auto& [nnode, dcost] : graph[cnode]) {
            int ncost = ccost + dcost;
            if (ncost < dist[nnode]) {
                dist[nnode] = ncost;
                que.push({ncost, nnode});
            }
        }
    }

    if (dist.back() == INF) {
        cout << -1 << '\n';
    } else {
        cout << dist.back() << '\n';
    }

    return 0;
}