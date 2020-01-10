#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int ans;

    if(a<=b) {
        if(c<=a) ans = a;
        else if(c>=a){
            if(c<=b) ans = c;
            else if(c>=b) ans = b;
        }
    }

    else if(a>=b) {
        if(c>=a) ans = a;
        else if(c<=a){
            if(c<=b) ans = b;
            else if(c>=b) ans = c;
        }
    }

    cout << ans;
    return 0;
}