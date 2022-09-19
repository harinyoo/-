#include <iostream>

using namespace std;

int main() {
    int x, y;
    int factor, multiple;
    int i;

    cin >> x >> y;
    if(x < y) {
        factor = x;
        multiple = y;
    }
    else {
        factor = y;
        multiple = x;
    }
    for(i=factor; i>0; i--) {
        if(x%i==0 && y%i==0) {
            factor = i;
            break;
        }
    }
    for(i=multiple; i<=x*y; i++) {
        if(i%x==0 && i%y==0) {
            multiple = i;
            break;
        }
    }

    cout << factor << endl << multiple << endl;
    return 0;
}