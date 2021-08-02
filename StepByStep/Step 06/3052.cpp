#include <iostream>
using namespace std;

int main() {
    int arr[10];
    int remainder[10];
    int cnt[42] = {0};
    int ans = 0;

    for(int i=0; i<10; i++) {
        cin >> arr[i];
        remainder[i] = arr[i] % 42;
    }

    for(int j=0; j<10; j++) {
        for(int k=0; k<42; k++) {
            if (remainder[j] == k) cnt[k]++;
        }
    }

    for(int l=0; l<42; l++) {
        if(cnt[l] != 0) ans++;
    }
    cout << ans;

    return 0;
}