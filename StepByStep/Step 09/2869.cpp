#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b, v;
    cin >> a >> b >> v;

    double x = (double)(v-a)/(double)(a-b);
    int days =  ceil(x) + 1;

    cout << days;
    return 0;
}