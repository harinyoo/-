#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    if(N==1) cout << 1;
    else {
        int i=1;
        while(N<3*(i-1)*i+2 || 3*i*(i+1)+2<=N) { i++; }
        cout << i+1;
    }
    return 0;
}