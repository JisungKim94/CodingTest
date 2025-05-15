#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double a, d, k;
    cin >> a >> d >> k;

    vector<double> dp;
    double per = d / 100.0;
    double remain = 1.0;
    double answer = 0.0;
    dp.push_back({0.0});
    int i = 1;
    while(1) {
        if (i > 1) {
            per = min(1.0, per * (1.0 + k/100.0));
        }
        dp.push_back({(remain * per)});
        answer += dp[i] * (a * i);
        remain -= dp[i];
        if (remain <= 0) break;
        i+=1;
    }
    cout << fixed << setprecision(6) << answer;
    return 0;
}
