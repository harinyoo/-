#include <iostream>
using namespace std;

#define SIZE 8
int N, M;
int arr[SIZE];
int picked[SIZE];

void tree( int cnt) {
    int i;
    if(cnt == M) {
        for(i=0; i<M; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
        return;
    }

    for(i=1; i<=N; i++) {
        if(picked[i]<=M) {
            picked[i]++;
            arr[cnt] = i;
            tree(cnt+1);
            picked[i]--;
        }
    }
}

int main() {
    int i;

    cin >> N >> M;
    for(i=0; i<M; i++) {
        arr[i] = 0;
        picked[i] = 0;
    }

    tree(0);
    return 0;
}