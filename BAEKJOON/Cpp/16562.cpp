#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

vector<int> parent;

// 재귀적 경로 압축 함수
int findRoot(int x) {
    if (parent[x] == x) 
        return x;
    return parent[x] = findRoot(parent[x]);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K;
    cin >> N >> M >> K;
    
    vector<int> A(N+1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }

    vector<pair<int,int>> relationship;
    relationship.reserve(M);
    for (int i = 0; i < M; ++i) {
        int v, w;
        cin >> v >> w;
        relationship.emplace_back(v, w);
    }

    // Union-Find 초기화
    vector<int> rank(N+1, 0);
    parent.resize(N+1);
    iota(parent.begin(), parent.end(), 0);

    auto unite = [&](int u, int v) {
        u = findRoot(u);
        v = findRoot(v);
        if (u == v) return;
        if (rank[u] < rank[v]) swap(u, v);
        parent[v] = u;
        if (rank[u] == rank[v]) ++rank[u];
    };

    // 친구 관계로 합치기
    for (auto &rel : relationship) {
        unite(rel.first, rel.second);
    }

    const int INF = 1e9;
    vector<int> minCost(N+1, INF);
    for (int i = 1; i <= N; ++i) {
        int r = findRoot(i);
        minCost[r] = min(minCost[r], A[i]);
    }

    int answer = 0;
    for (int i = 1; i <= N; ++i) {
        if (findRoot(i) == i) {
            answer += minCost[i];
        }
    }

    if (answer <= K) 
        cout << answer << '\n';
    else 
        cout << "Oh no\n";

    return 0;
}
