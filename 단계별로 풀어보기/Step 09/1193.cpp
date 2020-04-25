#include <iostream>
using namespace std;

int main() {
    int X;
    cin >> X;

    if(X==1) cout << 1 << "/" << 1;
    else {
        int i=1;
        while(X<2+(i+2)*(i-1)/2 || 2+(i+3)*i/2<=X){ i++; }
        int a = X-(2+(i+2)*(i-1)/2);
        if((i+2)%2 == 0) cout << i+1-a << "/" << 1+a;
        else cout << 1+a << "/" << i+1-a;
        }
    return 0;
}