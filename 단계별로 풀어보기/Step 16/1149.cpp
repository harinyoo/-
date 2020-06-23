#include <iostream>
using namespace std;

int main() {
    int N;
    int table [1000][3];
    int price [1000][3];
    int i;
    int minNum = __INT_MAX__;

    cin >> N;
    for(i=0; i<N; i++) {
        scanf("%d %d %d", &table[i][0], &table[i][1], &table[i][2]);
    }

    price [0][0] = table[0][0];
    price [0][1] = table[0][1];
    price [0][2] = table[0][2];

    for(i=1; i<N; i++) {
        price[i][0] = min(price[i-1][1], price[i-1][2]) + table[i][0];
        price[i][1] = min(price[i-1][0], price[i-1][2]) + table[i][1];
        price[i][2] = min(price[i-1][0], price[i-1][1]) + table[i][2];
    }

    for(i=0; i<3; i++) {
        if(price[N-1][i] < minNum)
            minNum = price[N-1][i];
    }
    printf("%d\n", minNum);
    return 0;
}