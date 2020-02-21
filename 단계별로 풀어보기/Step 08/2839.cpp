#include <iostream>
using namespace std;

int main() {
    int weight;
    cin >> weight;

    int x = 0;
    int y = 0;
    while(x < weight/3+1) {
        y = (weight-3*x)%5;
        if(y == 0) break;
        x++;
    }
    if(x == weight/3+1) cout << "-1";
    else cout << x + (weight-3*x)/5;
    return 0;
}