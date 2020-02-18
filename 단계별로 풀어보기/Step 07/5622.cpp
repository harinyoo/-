#include <iostream>
#include <vector>
using namespace std;

int main() {
    string str;
    cin >> str;

    vector<string> dial = {{"-1"}, {"-1"}, {"-1"}, {"ABC"}, {"DEF"}, {"GHI"},
                           {"JKL"}, {"MNO"}, {"PQRS"}, {"TUV"}, {"WXYZ"}};

    int sec = 0;
    for(int i=0; str[i]; i++) {
        for(int j=0; j<dial.size(); j++) {
            if(dial[j].find(str[i]) != string::npos) sec += j;
        }
    }
    cout << sec;
    return 0;
}