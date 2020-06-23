#include <iostream>

using namespace std;

int main() {
    int n;
    int arr[501][501];
    int sum[501][501];
    int result = -2147483648;
    int i, j;
    int x, y;

    cin >> n;
    for(i=1; i<=n; i++) {
        for(j=1; j<=i; j++) {
            cin >> arr[i][j];
        }
    }

    sum[1][1] = arr[1][1];
    for(i=2; i<=n; i++) {
        for(j=1; j<=i; j++) {
            if(j==1)
                sum[i][j] = sum[i-1][j] + arr[i][j];
            else if(j==i)
                sum[i][j] = sum[i-1][j-1] + arr[i][j];
            else{
                x = sum[i-1][j-1] + arr[i][j];
                y = sum[i-1][j] + arr[i][j];
                sum[i][j] = max(x, y);
            }
        }
    }

    for(i=1; i<=n; i++) {
        if(result < sum[n][i])
            result = sum[n][i];
    }
    printf("%d\n", result);
    return 0;
}