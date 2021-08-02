#include <iostream>
#include <cmath>
using namespace std;

void hanoi(int n, int from, int tmp, int to){
    if(n==1) printf("%d %d\n", from, to);
    else{
        hanoi(n-1, from, to, tmp);
        printf("%d %d\n", from, to);
        hanoi(n-1, tmp, from, to);
    }
}

int main() {
    int N;
    cin >> N;

    int cnt = pow(2,N)-1;
    cout << cnt <<  endl;

    hanoi(N,1,2,3);

    return 0;
}