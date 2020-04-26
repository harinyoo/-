#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int i, j=0;
    for(i=0; i<N; i++) {
        for(j=0; j<i+1; j++) cout << "*";
        cout << endl;
    }

    for(i=N-1; i>0; i--){
        for(j=0; j<i; j++) cout << "*";
        cout << endl;
    }
    return 0;
}