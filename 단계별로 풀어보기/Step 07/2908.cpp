#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    int a_ = a%10*100 + (a/10%10)*10 + a/100;
    int b_ = b%10*100 + (b/10%10)*10 + b/100;

    if(a_ > b_) cout << a_;
    else cout << b_;
    return 0;
}