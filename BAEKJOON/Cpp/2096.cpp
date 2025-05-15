#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int dp[2][3] = {};
    int dpmin[2][3] = {};

    for (int i = 0; i < n; ++i) {
        int a, b, c;
        cin >> a >> b >> c;

        if (i == 0) {
            dp[0][0] = dpmin[0][0] = a;
            dp[0][1] = dpmin[0][1] = b;
            dp[0][2] = dpmin[0][2] = c;
        } else {
            dp[i%2][0] = max(dp[(i-1)%2][0], dp[(i-1)%2][1]) + a;
            dp[i%2][1] = max({dp[(i-1)%2][0], dp[(i-1)%2][1], dp[(i-1)%2][2]}) + b;
            dp[i%2][2] = max(dp[(i-1)%2][1], dp[(i-1)%2][2]) + c;

            dpmin[i%2][0] = min(dpmin[(i-1)%2][0], dpmin[(i-1)%2][1]) + a;
            dpmin[i%2][1] = min({dpmin[(i-1)%2][0], dpmin[(i-1)%2][1], dpmin[(i-1)%2][2]}) + b;
            dpmin[i%2][2] = min(dpmin[(i-1)%2][1], dpmin[(i-1)%2][2]) + c;
        }
    }

    int last = (n - 1) % 2;
    cout << *max_element(dp[last], dp[last] + 3) << ' ';
    cout << *min_element(dpmin[last], dpmin[last] + 3) << '\n';

    return 0;
}
