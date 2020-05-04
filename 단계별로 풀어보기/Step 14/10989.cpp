#include <iostream>
using namespace std;

int main() {
    int N, num;
    int i, j;
    int arr[10001];
    fill_n(arr, 10001, 0);

    scanf("%d", &N);
    for(i=0; i<N; i++) {
        scanf("%d", &num);
        arr[num]++;
    }

    for(i=1; i<10001; i++) {
        for(j=0; j<arr[i]; j++) {
            printf("%d\n", i);
        }
    }
    return 0;
}