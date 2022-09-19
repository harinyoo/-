#include <iostream>

using namespace std;

int main() {
    int n;
    int stairs[301];
    int score[301];
    int i;

    cin >> n;
    for(i=1; i<=n; i++) {
        cin >> stairs[i];
    }

    score[1] = stairs[1];
    score[2] = max(stairs[2], score[1]+stairs[2]);
    score[3] = max(score[1]+stairs[3], stairs[2]+stairs[3]);

    for(i=4; i<=n; i++) {
        score[i] = max(score[i-2]+stairs[i], score[i-3]+stairs[i-1]+stairs[i]);
    }
    cout << score[n] << endl;
    return 0;
}