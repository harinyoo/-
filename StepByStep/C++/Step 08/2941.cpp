#include <iostream>
#include <vector>
using namespace std;

int main() {
    string str;
    cin >> str;

    vector<string> croatian ={"c=", "c-", "dz=", "d-",
                              "lj", "nj", "s=", "z="};
    size_t pos = 0;
    for(int i=0; i<croatian.size(); i++) {
        pos = str.find(croatian[i]);
        for(; pos!=string::npos; pos=str.find(croatian[i])) {
            str.replace(pos, croatian[i].length(), "/");
        }
    }
    cout << str.length();
    return 0;
}