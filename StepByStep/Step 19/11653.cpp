#include <cstdio>

using namespace std;

int main() {
    int N;
    int i = 2;

    scanf("%d", &N);
    while(2<=N) {
        if(N%i==0) {
            printf("%d\n", i);
            N /= i;
            continue;
        }
        i++;
    }
    return 0;
}