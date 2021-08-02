#include <iostream>

using namespace std;

int arr[2][12];

int main() {
    int N;
    int i, j;
    long sum = 0;

    cin >> N;
    for(i=2; i<=10; i++) {
        arr[1][i] = 1;
    }

    for(i=2; i<=N; i++) {
        for(j=1; j<=10; j++) {
            arr[i%2][j] = (arr[(i+1)%2][j-1]+arr[(i+1)%2][j+1])%1000000000;
        }
    }

    for(i=1; i<=10; i++) {
       sum += arr[N%2][i];
    }

    cout << sum%1000000000 << endl;
    return 0;
}