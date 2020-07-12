#include <iostream>
using namespace std;

int weight[101];
int value[101];
int dp[101][100001];

int main() {
    int N, K;
    int i, j;

    cin >> N >> K;
    for(i=1; i<=N; i++) {
        cin >> weight[i] >> value[i];
    }

    for(i=1; i<=N; i++) {
        for(j=1; j<=K; j++) {
            dp[i][j] = dp[i-1][j];
            if(j-weight[i] >= 0)
                dp[i][j] = max(dp[i][j], dp[i-1][j-weight[i]]+value[i]);
        }
    }

    cout << dp[N][K] << endl;
    return 0;
}
