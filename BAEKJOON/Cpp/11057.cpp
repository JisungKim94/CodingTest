#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

const int MOD = 10007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> dp(10, 1), tmp(10);

    for (int len = 2; len <= N; ++len) {
        int sum = 0;
        for (int d = 0; d < 10; ++d) {
            sum = (sum + dp[d]) % MOD;
            tmp[d] = sum;
        }
        dp = tmp;
    }

    int answer = accumulate(dp.begin(), dp.end(), 0) % MOD;
    cout << answer;
    return 0;
}
