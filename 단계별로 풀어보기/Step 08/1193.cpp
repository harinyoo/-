#include <iostream>
using namespace std;

int main() {
    int num;
    cin >> num;

    int x = 2;
    while(num<(x-1)*(x-2)/2+1 || x*(x-1)/2<num) { x++; }

    int below=1, above=1;
    if(x%2 == 0) {
        below = num - ((x-1)*(x-2)/2+1) + 1;
        above = x - below;
    }
    else if(x%2 != 0) {
        above = num - ((x-1)*(x-2)/2+1) + 1;
        below = x - above;
    }

    cout << above << "/" << below;
    return 0;
}