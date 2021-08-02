#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    string str;
    cin >> str;

    int sum = 0;
    int i;
    for(i=0; i<N; i++) {
        sum += str.at(i)-'0';
    }
    cout << sum;
    return 0;
}