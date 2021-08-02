#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    int b1 = b/100;
    int b2 = (b-b1*100)/10;
    int b3 = b-b1*100-b2*10;

    cout << a*b3 << endl;
    cout << a*b2 << endl;
    cout << a*b1 << endl;
    cout << a*b3+a*b2*10+a*b1*100;
    return 0;
}