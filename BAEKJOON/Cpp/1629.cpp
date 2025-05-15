#include <iostream>
using namespace std;

// a^b = a^(bin(b))
// e.g. a^13 = a^(1101) = a^(8+4+0+1) = 해당하는 거듭제곱 꼴만 곱하면 단순 제곱(a^(+1)반복)에 비해 연산이 획기적으로 줄어든다.
long mod_pow(long a, long b, long m) {
    long result = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) {
            result = (result * a) % m;
        }
        a = (a * a) % m;
        b >>= 1;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long A, B, C;
    cin >> A >> B >> C;
    cout << mod_pow(A, B, C) << "\n";
    return 0;
}
