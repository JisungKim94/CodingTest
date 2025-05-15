#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r,c;
    cin >> r >> c;
    vector<vector<int>> table(r,vector<int>(c,0));
    int desertCnt = 0;
    int regularCnt = 0;
    int fertileCnt = 0;
    int minValueExceptDesert = 100;
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            cin >> table[i][j];
            if (table[i][j] == 0) {
                desertCnt+=1;
            } else {
                minValueExceptDesert = min(minValueExceptDesert, table[i][j]);
                if (table[i][j] == 1) {regularCnt += 1;}
                if (table[i][j] == 2) {fertileCnt += 1;}
            }
        }
    }

    // guard clause
    if (desertCnt >= 2) {
        cout<<0;
        return 0;
    }
    if (desertCnt == 1) {
        if (minValueExceptDesert == 0) {
            cout<<0;    
        }
        if (minValueExceptDesert == 1) {
            if (r==1) {
                // cout<< table[0][0]<<endl;
                // cout<< table[0][table[0].size()-1]<<endl;
                if (table[0][0] == 1 || table[0][table[0].size()-1] == 1) {
                    cout<<1;
                    return 0;
                }
                else {cout<<2; return 0;}
            }
            if (c==1) {
                // cout<< table[0][0]<<endl;
                // cout<< table[table.size()-1][0]<<endl;
                if (table[0][0] == 1 || table[table.size()-1][0] == 1) {
                    cout<<1;
                    return 0;
                }
                else {cout<<2; return 0;}
            }
            cout<<1;
            return 0;
        }
        if (minValueExceptDesert == 2) {
            cout<<2;    
        }
        return 0;
    }

    // cout<<fertileCnt%2<<", "<<fertileCnt/2<<endl;
    if (fertileCnt%2) {
        cout<<long(powl(2,fertileCnt/2));
    } else {
        cout<<0;
    }
    return 0;
}
