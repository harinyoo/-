#include <iostream>
using namespace std;

bool arr[1000001];

int main() {
    int M, N;
    cin >> M >> N;

    arr[0] = false;
    arr[1] = false;
    int i, j;
    for(i=2; i<1000001; i++) arr[i] = true;

    for(i=2; i*i<=1000000; i++) {
        if(arr[i]){
            for(j=i+i; j<=1000000; j+=i) {
                arr[j] = false;
            }
        }
    }

    for(i=M; i<=N; i++) {
        if(arr[i]) printf("%d\n", i);
    }
    return 0;
}