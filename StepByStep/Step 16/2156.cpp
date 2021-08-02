#include <iostream>
using namespace std;

int main() {
    int n;
    int wine[10003];
    int dp[10003];
    int i;

    cin >> n;
    for(i=3; i<=n+2; i++) {
        cin >> wine[i];
    }

    for(i=3; i<=n+2; i++) {
        dp[i] = max(dp[i-1], wine[i]+dp[i-2]);
        dp[i] = max(dp[i], wine[i]+wine[i-1]+dp[i-3]);
    }

    cout << dp[n+2] << endl;
    return 0;
}