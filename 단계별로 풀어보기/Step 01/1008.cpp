#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    long double result;
    result = (long double) A/B;

    //cout.setf(ios::fixed);
    cout.precision(19);
    //cout.precision(dbl::max_digits10);
    cout << result;

    return 0;
}