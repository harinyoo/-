#include <iostream>
using namespace std;

#define SIZE 9

void tree(int N, int M, int cnt, int *arr, bool *visited) {
    int i;
    if(cnt == M) {
        for(i=0; i<M; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
        return;
    }
    for(i=1; i<=N; i++) {
        if(!visited[i]) {
            visited[i] = true;
            arr[cnt] = i;
            tree(N, M, cnt+1, arr, visited);
            visited[i] = false;
        }
    }
}

int main() {
    int N, M, i;
    int arr[SIZE];
    bool visited[SIZE];

    cin >> N >> M;
    for(i=0; i<SIZE; i++) {
        arr[i] = 0;
        visited[i] = false;
    }
    tree(N, M, 0, arr, visited);
    return 0;
}