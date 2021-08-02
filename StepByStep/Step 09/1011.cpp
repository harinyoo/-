#include <iostream>
#include <cmath>
using namespace std;

int count(int x, int y) {
    int dis = y-x;
    int tmp = floor(sqrt(dis));

    double a = pow(tmp, 2);
    double b = pow(tmp+1,2);
    if(a == dis) return 2*tmp-1;
    else {
        if((a+b)/2 < dis) return 2*tmp+1;
        else return 2*tmp;
    }
}
int main() {
    int t, x, y;
    cin >> t;

    for(int i=0; i<t; i++) {
        cin >> x >> y;
        cout << count(x, y) << endl;
    }
    return 0;
}