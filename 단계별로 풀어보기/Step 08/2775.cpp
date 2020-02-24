#include <iostream>
using namespace std;

int people(int k, int n) {
    int apt[15][14] = {0};
    int i;
    for(i=0; i<n; i++) {
        apt[0][i] = i+1;
    }

    for(i=1; i<=k; i++) {
        apt[i][0] = 1;
        for(int j=1; j<n; j++) {
            apt[i][j] = apt[i][j-1] + apt[i-1][j];
        }
    }

    return apt[k][n-1];
}

int main() {
    int t, k, n;
    cin >> t;
    for(int i=0; i<t; i++) {
        cin >> k >> n;
        cout << people(k, n) << endl;
    }
    return 0;
}