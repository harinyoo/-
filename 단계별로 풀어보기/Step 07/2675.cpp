#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    for(int i=0; i<t; i++) {
        int r;
        cin >> r;
        string str;
        cin >> str;
        for(int j=0; j<str.length(); j++) {
            for(int k=0; k<r; k++){
                cout << str[j];
            }
        }
        cout << endl;
    }
    return 0;
}
