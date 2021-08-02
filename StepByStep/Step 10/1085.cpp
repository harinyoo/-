#include <iostream>
using namespace std;

int main() {
    int x, y, w, h;
    cin >> x >> y >> w >> h;

    int dis1 = x;
    int dis2 = y;
    if(x*2>w) dis1 = w-x;
    if(y*2>h) dis2 = h-y;

    if(dis1 < dis2) cout << dis1;
    else cout << dis2;
    return 0;
}