#include <iostream>
using namespace std;

bool han(int n) {
    if(n<100) return true;
    else if(n>=100) {
        int x = n/100-(n/10)%10;
        int y = (n/10)%10-n%10;
        if(x==y) return true;
        else return false;
    }
}

int main() {
    int n;
    cin >> n;

    int cnt = 0;
    int i;
    for(i=1; i<=n; i++) {
        if(han(i)) cnt++;
    }
    cout << cnt;
    return 0;
}