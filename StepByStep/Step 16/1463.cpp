#include <iostream>
using namespace std;

int main() {
    int n;
    int i;
    int arr[1000001];

    arr[0] = 0;
    arr[1] = 0;
    arr[2] = 1;
    arr[3] = 1;

    cin >> n;
    for(i=4; i<=n; i++) {
        arr[i] = arr[i-1] + 1;
        if (i % 2 == 0)
            arr[i] = min(arr[i], arr[i/2] + 1);
        if (i % 3 == 0)
            arr[i] = min(arr[i], arr[i/3] + 1);
    }

    cout << arr[n] << endl;
    return 0;
}