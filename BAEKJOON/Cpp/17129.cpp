#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m;
vector<vector<int>> A;
vector<vector<int>> visited;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

bool isIn(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

int bfs(int sx, int sy) {
    queue<pair<int, int>> q;
    q.push({sx, sy});
    visited[sx][sy] = 1;

    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        if (A[x][y] == 3 || A[x][y] == 4 || A[x][y] == 5) {
            return visited[x][y] - 1; // 첫 칸 제외한 이동 횟수
        }
        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if (isIn(nx, ny) && !visited[nx][ny] && A[nx][ny] != 1) {
                visited[nx][ny] = visited[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    A.assign(n, vector<int>(m));
    visited.assign(n, vector<int>(m, 0));

    int sx = -1, sy = -1;
    for (int i = 0; i < n; ++i) {
        string row;
        cin >> row;
        for (int j = 0; j < m; ++j) {
            A[i][j] = row[j] - '0';
            if (A[i][j] == 2) {
                sx = i;
                sy = j;
            }
        }
    }

    int result = bfs(sx, sy);
    if (result != -1) {
        cout << "TAK\n" << result;
    } else {
        cout << "NIE\n";
    }

    return 0;
}
