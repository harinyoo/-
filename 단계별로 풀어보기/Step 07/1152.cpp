#include <iostream>
using namespace std;

int main() {
    string str;
    getline(cin, str);

    int i;
    int cnt = 0;
    for(i=0; i<str.length(); i++) {
        if(str[i] == ' ') cnt++;
    }

    if(str[0] == ' ') cnt--;
    if(str[str.length()-1] == ' ') cnt--;

    cout << cnt+1;
    return 0;
}