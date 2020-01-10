#include <iostream>
#include <string>
using namespace std;

int main() {
    int test;
    cin >> test;

    char result[1000][160] = {"\0"};
    for(int i=0; i<test; i++) {
        int repeat;
        cin >> repeat;
        string str;
        cin >> str;
        for(int j=0; j<str.size(); j++) {
            for(int k=0; k<repeat; k++) {
                result[i][j*repeat+k] = str[j];
            }
        }
    }

    for(int l=0; l<test; l++){
        for(int m=0; m<160; m++){
            if(result[l][m] != NULL) cout << result[l][m];
        }
        cout << endl;
    }
    return 0;
}