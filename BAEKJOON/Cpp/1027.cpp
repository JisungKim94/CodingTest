#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> h(N);
    for (int i = 0; i < N; i++) {
        cin >> h[i];
    }

    int answer = 0;
    for (int i = 0; i < N; i++) {
        int visible = 0;
        double maxL = -1e18, maxR = -1e18;

        // to the left
        for (int j = i - 1; j >= 0; j--) {
            double slope = double(h[j] - h[i]) / (i - j);
            if (slope > maxL) {
                maxL = slope;
                visible++;
            }
        }

        // to the right
        for (int j = i + 1; j < N; j++) {
            double slope = double(h[j] - h[i]) / (j - i);
            if (slope > maxR) {
                maxR = slope;
                visible++;
            }
        }

        answer = max(answer, visible);
    }

    cout << answer << "\n";
    return 0;
}
