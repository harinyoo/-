#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int i, j, result = N;
    int cycle=0;
    do {
        i = result/10;
        j = result%10;
        result = j*10 + (i+j)%10;
        cycle++;
    } while(result != N);

    cout << cycle;
    return 0;
}