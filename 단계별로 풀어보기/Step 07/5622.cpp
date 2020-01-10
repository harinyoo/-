#include <iostream>
using namespace std;

int main() {
    string str;
    cin >> str;

    int sec = 0;
    for(int i=0; i<str.size(); i++) {
        if(str[i]>='A' && str[i]<='O') sec += (str[i]+1)/3-19;
        else if(str[i]>='P' && str[i]<='S') sec += 8;
        else if(str[i]>='T' && str[i]<='V') sec += 9;
        else if(str[i]>='W' && str[i]<='Z') sec += 10;
    }

    cout << sec;
    return 0;
}
