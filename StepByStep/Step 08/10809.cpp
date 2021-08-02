#include <iostream>
using namespace std;

int main() {
    string str;
    cin >> str;
    
    char alphabet[26];
    for(int i=0; i<26; i++) {
        alphabet[i] = 'a'+i;
    }
    
    int cnt[26];
    fill_n(cnt, 26, -1);
    
    for(int j=0; j<str.length(); j++) {
        for(int k=0; k<26; k++) {
            if(str[j] == alphabet[k]) {
                alphabet[k] = '0';
                cnt[k] = j;
            }
        }
    }
    
    for(int l=0; l<26; l++) {
        cout << cnt[l] << " ";
    }
    return 0;
}
