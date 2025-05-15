#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    int MAX = 100001;
    vector<int> answers(MAX, MAX);
    deque<int> dq;

    answers[N] = 0;
    dq.push_back(N);

    while (!dq.empty()) {
        int curr = dq.front();
        if (curr == K) break;
        dq.pop_front();

        int jump = curr * 2;
        if (jump < MAX && answers[jump] > answers[curr]) {
            answers[jump] = answers[curr];
            dq.push_front(jump);
        }

        for (int next : {curr - 1, curr + 1}) {
            if (next >= 0 && next < MAX && answers[next] > answers[curr] + 1) {
                answers[next] = answers[curr] + 1;
                dq.push_back(next);
            }
        }
    }

    cout << answers[K];
    return 0;
}
