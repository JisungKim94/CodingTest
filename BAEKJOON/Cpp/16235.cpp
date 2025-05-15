#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K;
    cin >> N >> M >> K;

    vector<vector<int>> A(N, vector<int>(N)); // 겨울 양분 정보
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            cin >> A[i][j];

    vector<vector<deque<int>>> trees(N, vector<deque<int>>(N)); // 칸별 나무 나이 저장
    for (int i = 0; i < M; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        trees[x - 1][y - 1].push_back(z);
    }

    vector<vector<int>> land(N, vector<int>(N, 5)); // 초기 양분 5
    vector<pair<int, int>> dirs = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};

    while (K--) {
        // --- 봄 ---
        vector<vector<vector<int>>> dead(N, vector<vector<int>>(N)); // 죽은 나무
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                deque<int> survived;
                for (int age : trees[i][j]) {
                    if (land[i][j] >= age) {
                        land[i][j] -= age;
                        survived.push_back(age + 1);
                    } else {
                        dead[i][j].push_back(age);
                    }
                }
                trees[i][j] = survived;
            }
        }

        // --- 여름 ---
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                for (int age : dead[i][j])
                    land[i][j] += age / 2;

        // --- 가을 ---
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                for (int age : trees[i][j]) {
                    if (age % 5 == 0) {
                        for (auto [dx, dy] : dirs) {
                            int ni = i + dx, nj = j + dy;
                            if (ni >= 0 && ni < N && nj >= 0 && nj < N) {
                                trees[ni][nj].push_front(1); // 어린 나무 앞에 삽입
                            }
                        }
                    }
                }
            }
        }

        // --- 겨울 ---
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                land[i][j] += A[i][j];
    }

    int answer = 0;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            answer += trees[i][j].size();

    cout << answer << '\n';
    return 0;
}
