#include <iostream>
using namespace std;

#define SIZE 9
int N, M;
int arr[SIZE];
bool visited[SIZE];

void tree(int cnt) {
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
            if(arr[cnt-1] < i) {
                arr[cnt] = i;
                tree(cnt+1);
            }
            visited[i] = false;
        }
    }
}

int main() {
    int i;

    cin >> N >> M;
    for(i=0; i<SIZE; i++) {
        arr[i] = 0;
        visited[i] = false;
    }

    tree(0);
    return 0;
}