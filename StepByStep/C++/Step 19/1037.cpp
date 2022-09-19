#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N;
    int factor[50];
    int i;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> factor[i];
    }
    sort(factor, factor+N);
    cout << factor[0]*factor[N-1] << endl;
    return 0;
}