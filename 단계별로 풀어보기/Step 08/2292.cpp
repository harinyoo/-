#include <iostream>
using namespace std;

int main() {
    int num;
    cin >> num;

    int cnt;
    if(num==1) cnt = 1;
    else {
        int x = (num-2)/6;
        int idx = 2;
        while(x<(idx-1)*(idx-2)/2 || idx*(idx-1)/2-1<x) { idx++; }
        cnt = idx;
    }

    cout << cnt;
    return 0;
}