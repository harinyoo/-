#include <iostream>
using namespace std;

int main() {
    string str;
    cin >> str;

    for(int i=0; i<str.length(); i++) {
        if(str[i]>='a') str[i] -= 32;
    }

    char alphabet[26];
    for(int j=0; j<26; j++) alphabet[j] = 'A'+j;

    int cnt[26]={0};
    for(int k=0; k<str.length(); k++) {
        for(int l=0; l<26; l++) {
            if(str[k]==alphabet[l]) cnt[l]++;
        }
    }

    int max = cnt[0];
    int idx = 0;
    for(int m=0; m<26; m++) {
        if(max<cnt[m]) {
            max = cnt[m];
            idx = m;
        }
    }

    int tmp=0;
    for(int n=0; n<26; n++) {
        if(max==cnt[n]) tmp++;
    }

    if(tmp==1) cout << alphabet[idx];
    else cout << "?";
    return 0;
}
