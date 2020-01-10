#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cin >> str;
    for(int i=0; i<str.size(); i++) {
        if(str[i]>=97 && str[i]<=122) str[i] -= 32;
    }

    char alphabet[26];
    for(int j=0; j<26; j++) {
        alphabet[j] = 'A'+j;
    }

    int alpha_num[26] = {0};
    for(int k=0; k<str.size(); k++) {
        for(int l=0; l<26; l++){
            if(str[k]==alphabet[l]) alpha_num[l]++;
        }
    }

    int max = alpha_num[0];
    int idx = 0;
    for(int m=0; m<26; m++) {
        if(max < alpha_num[m]) {
            max = alpha_num[m];
            idx = m;
        }
    }

    int cnt = 0;
    for(int n=0; n<26; n++) {
        if(max == alpha_num[n]) cnt++;
    }
    if(cnt == 1) cout << alphabet[idx];
    else cout << "?";
    return 0;
}
