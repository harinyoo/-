#include <iostream>
using namespace std;

int main() {
    string str;
    getline(cin, str);

    int cnt = 0;
    int i;
    for(i=0; i<str.size(); i++) {
        if(str.at(i) == ' ') cnt++;
    }

    if(str.at(0) ==' ') cnt--;
    if(str.at(str.size()-1)==' ') cnt--;

    cout << cnt+1;
    return 0;
}