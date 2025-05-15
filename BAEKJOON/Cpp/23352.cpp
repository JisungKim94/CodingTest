#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int N, M;
vector<vector<int>> table;
int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

pair<int,int> bfs(int si, int sj) {
    vector<vector<bool>> visited(N, vector<bool>(M, false));
    vector<vector<int>>  cost(N, vector<int> (M, 0));
    deque<pair<int,int>> q;

    visited[si][sj] = true;
    cost[si][sj] = 0;
    q.emplace_back(si, sj);

    int localMaxCost = 0;
    int localEndCost = table[si][sj];

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop_front();
        int ccost = cost[r][c];

        if (ccost > localMaxCost) {
            localMaxCost = ccost;
            localEndCost = table[r][c];
        }
        else if (ccost == localMaxCost && table[r][c] > localEndCost) {
            localEndCost = table[r][c];
        }

        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            if (!visited[nr][nc] && table[nr][nc] != 0) {
                visited[nr][nc] = true;
                cost[nr][nc]    = ccost + 1;
                q.emplace_back(nr, nc);
            }
        }
    }

    return {localMaxCost, localEndCost};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    table.assign(N, vector<int>(M));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> table[i][j];
        }
    }

    int globalMaxDist = -1;
    int globalAns     =  0;

    for (int si = 0; si < N; si++) {
        for (int sj = 0; sj < M; sj++) {
            if (table[si][sj] == 0) continue;

            auto [localMaxCost, localEndCost] = bfs(si, sj);
            int sum = table[si][sj] + localEndCost;

            if (localMaxCost > globalMaxDist) {
                globalMaxDist = localMaxCost;
                globalAns = sum;
            }
            else if (localMaxCost == globalMaxDist && sum > globalAns) {
                globalAns = sum;
            }
        }
    }

    cout << globalAns;
    return 0;
}
