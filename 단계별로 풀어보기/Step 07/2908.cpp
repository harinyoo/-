#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;

    int tmp1, tmp2, tmp3;
    tmp1 = A/100;
    tmp2 = (A%100)/10;
    tmp3 = (A%100)%10;
    A = tmp3*100 + tmp2*10 + tmp1;

    tmp1 = B/100;
    tmp2 = (B%100)/10;
    tmp3 = (B%100)%10;
    B = tmp3*100 + tmp2*10 + tmp1;

    if(A>B) cout << A;
    else cout << B;

    return 0;
}