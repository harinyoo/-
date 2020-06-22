#include <iostream>
using namespace std;

int main() {
    int T;
    int N;
    int i;
    long arr[101];

    arr[0] = 0;
    arr[1] = 1;
    arr[2] = 1;

    for(i=3; i<101; i++) {
        arr[i] = arr[i-2]+arr[i-3];
    }

    cin >> T;
    for(i=0; i<T; i++) {
        cin >> N;
        printf("%ld\n", arr[N]);
    }
    return 0;
}