#include <iostream>
#include <cmath>
using namespace std;

int check(int x1, int y1, int r1, int x2, int y2, int r2){
    int distance = pow(x1-x2,2)+pow(y1-y2,2);
    int length1 = pow(r1+r2,2);
    int length2 = pow(r1-r2,2);

    if(x1==x2 && y1==y2 && r1==r2) return -1;
    else if(length1 == distance) return 1;
    else if(length1 < distance) return 0;
    else if(length1 > distance) {
        if(length2 < distance) return 2;
        else if(length2 == distance) return 1;
        else if(length2 > distance) return 0;
    }
}

int main() {
    int T;
    cin >> T;

    int i;
    int x1, y1, r1, x2, y2, r2;
    for(i=0; i<T; i++) {
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        cout << check(x1, y1, r1, x2, y2, r2) << endl;
    }
    return 0;
}