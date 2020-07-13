#include <iostream>
using namespace std;


int main() {
    string str;
    string tmp = "";
    bool minus = false;
    int result = 0;
    int i;

    cin >> str;
    for(i=0; i<=str.length(); i++) {
        if(str[i]=='-' || str[i]=='+' || str[i]=='\0') {
            if(minus)
                result -= stoi(tmp);
            else
                result += stoi(tmp);
            tmp = "";

            if(str[i]=='-')
                minus = true;
            continue;
        }
        tmp += str[i];
    }

    cout << result << endl;
    return 0;
}