#include <iostream>
#include <vector>
using namespace std;

int i, j;
bool arr[10001];

void prime(){
    arr[0] = false;
    arr[1] = false;

    for(i=2; i<10001; i++) arr[i] = true;
    for(i=2; i*i<10001; i++) {
        if(arr[i]) {
            for(j=i+i; j<10001; j += i) arr[j] = false;
        }
    }
}
void goldbach(int n){
    int partition1, partition2;
    for(i=2; i*2<=n; i++) {
        if(arr[i]&&arr[n-i]) {
            partition1 = i;
            partition2 = n-i;
        }
    }
    cout << partition1 << " " << partition2 << endl;
}

int main() {
    int T;
    cin >> T;

    prime();
    int n, k;
    for(k=0; k<T; k++) {
        cin >> n;
        goldbach(n);
    }
    return 0;
}