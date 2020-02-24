#include <iostream>
using namespace std;

int room (int h, int w, int n) {
    int roomNum;
    int x = n / h;
    int y = n % h;

    if(y == 0) {
        roomNum = h*100 + x;
    }
    else {
        roomNum = y*100 + x + 1;
    }
    return roomNum;
}
int main() {
    int t, h, w, n;
    cin >> t;

    int i=0;
    for(i=0; i<t; i++) {
        cin >> h >> w >> n;
        cout << room(h, w, n) << endl;
    }
    return 0;
}