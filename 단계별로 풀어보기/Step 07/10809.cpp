#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cin >> str;

    char alphabet[26];
    for(int i=0; i<26; i++) {
        alphabet[i] = 'a'+i;
    }

    int alpha_num[26];
    for(int j=0; j<26; j++) alpha_num[j] = -1;

    for(int k=0; k<str.size(); k++) {
        for(int l=0; l<26; l++) {
            if(alpha_num[l]==-1){
                if(str[k]==alphabet[l]) alpha_num[l] = k;
            }
        }
    }
    for(int m=0; m<26; m++) {
        cout << alpha_num[m] << " ";
    }
    return 0;
}
