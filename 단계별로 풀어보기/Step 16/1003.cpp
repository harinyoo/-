#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T, N;
    int i, j;

    cin >> T;
    for(i=0; i<T; i++) {
        vector<int> zero;
        vector<int> one;

        zero.push_back(1);
        zero.push_back(0);
        one.push_back(0);
        one.push_back(1);

        scanf("%d", &N);
        for(j=2; j<=N; j++) {
            zero.push_back(zero[j-2]+zero[j-1]);
            one.push_back(one[j-2]+one[j-1]);
        }
        printf("%d %d\n", zero[N], one[N]);
    }
    return 0;
}

