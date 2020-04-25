#include <iostream>
using namespace std;

int people(int k, int n) {
    if(k==0) return n;
    if(n==1) return 1;
    return people(k, n-1) + people(k-1,n);
}

int main() {
    int T, k, n;
    cin >> T;

    int i;
    for(i=0; i<T; i++) {
        cin >> k >> n;
        cout << people(k, n) << endl;
    }
    return 0;
}