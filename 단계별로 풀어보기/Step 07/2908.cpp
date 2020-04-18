#include <iostream>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1 >> s2;

    string bigger;
    int i;
    for(i=2; i>=0; i--) {
        if(s1[i] > s2[i]) {
            bigger = s1;
            break;
        }
        else if(s1[i] < s2[i]) {
            bigger = s2;
            break;
        }
    }

    for(i=2; i>=0; i--) cout << bigger[i];
    return 0;
}