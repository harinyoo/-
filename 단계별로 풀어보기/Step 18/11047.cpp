#include <iostream>
using namespace std;

int main() {
    int N, K;
    int coin[10];
    int i;
    int cnt = 0;

    cin >> N >> K;
    for(i=0; i<N; i++) {
        cin >> coin[i];
    }

    while(0 < K) {
        for(i=0; i<N; i++) {
            if(K < coin[i])
                break;
        }
        K -= coin[i-1];
        cnt++;
    }

    cout << cnt << endl;
    return 0;
}