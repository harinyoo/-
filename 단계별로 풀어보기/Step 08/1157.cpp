#include <iostream>
using namespace std;

int main() {
    string str;
    cin >> str;

    int i;
    for(i=0; i<str.size(); i++) {
        if(str.at(i)>='a') str.at(i) -= 32;
    }

    int check[26];
    fill_n(check, 26, 0);
    for(i=0; i<str.size(); i++) {
        check[str.at(i)-'A']++;
    }

    int max = check[0];
    int idx = 0;
    for(i=0; i<26; i++) {
        if(max<check[i]) {
            max = check[i];
            idx = i;
        }
    }

    int cnt = 0;
    for(i=0; i<26; i++) {
        if(check[i] == max) cnt++;
    }

    if(cnt==1) cout << char(idx+'A');
    else cout << "?";
    return 0;
}