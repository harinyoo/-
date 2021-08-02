#include <iostream>
using namespace std;

bool arr[246913];
int main() {
    arr[0] = false;
    arr[1] = false;

    int i, j;
    for(i=2; i<246913; i++) {
        arr[i] = true;
    }

    for(i=2; i*i<246913; i++) {
        if(arr[i]){
            for(j=i+i; j<246913; j+=i) {
                arr[j] = false;
            }
        }
    }

    int n, cnt;
    while(cin >> n) {
        if(n==0) break;
        cnt = 0;
        for(i=n+1; i<=2*n; i++) {
            if(arr[i]) cnt++;
        }
        cout << cnt << endl;
    }
    return 0;
}
