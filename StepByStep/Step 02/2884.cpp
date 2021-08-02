#include <iostream>
using namespace std;

int main() {
    int hour, min;
    cin >> hour >> min;

    if(hour>0) {
        if(min<45) cout << hour-1 << " " << min+60-45;
        else cout << hour << " " << min-45;
    }
    else if(hour==0) {
        if(min<45) cout << 23 << " " << min+60-45;
        else cout << hour << " " << min-45;
    }
    return 0;
}