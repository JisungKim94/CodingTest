#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int N,K;
    cin >> N >> K;
    cin>>s;

    vector<int> v;
    for (int i = 0; i<s.size(); i++) {
        if (s[i] == 'A') v.push_back(s[i]-'A');
        else v.push_back('Z'-s[i]+1);
    }
    // for (int i = 0; i<v.size(); i++) {
    //     cout<<v[i]<<endl;
    // }
    // cout<<endl;
    // abcdefghijklmnopqrstuvwxyz (26 cycle)
    
    int sum = 0;
    int idx = 0;
    
    for (int i = 0; i<v.size(); i++) {
        sum+=v[i];
    }

    if (K>sum) {
        K=K-sum;
        for (int i = 0; i<v.size(); i++) {
            v[i] = 0;
        }
        K %= 26;
        v[v.size()-1] = (v[v.size()-1] + (26-K))%26;
    }
    else {
        // cout<<"ASDF"<<endl;
        while (idx<v.size() && K>0) {
            if (K>=v[idx]) {K-=v[idx], v[idx] = 0;}
            idx+=1;
        }
        if (K>0) {
            v[idx-1] = (v[idx-1] + (26-K))%26;
        }
    }
    // for (int i = 0; i<v.size(); i++) {
    //     cout<<v[i]<<endl;
    // }
    // cout<<endl;

    vector<char> S;
    for (int i = 0; i<v.size(); i++) {
        char c;
        if (v[i]==0) c = 'A';
        else c = static_cast<char>('Z'-v[i]+1);
        
        S.push_back(c);
        cout<<S[i];
    }
    

    // cout << "";
    return 0;
}
