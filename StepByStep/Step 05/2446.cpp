#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int i = 0;
    int j = 0;

    for(i=0; i<2*N-1; i++) {
        if(i<N) {
            for(j=0; j<i; j++) cout<<" ";
            for(j=0; j<(2*N-1-2*i); j++) cout<<"*";
            cout<<" ";
        }
        else if(i>=N) {
            for(j=0; j<(2*N-2-i); j++) cout<<" ";
            for(j=0; j<(2*i-2*N+3); j++) cout<<"*";
            cout<<" ";
        }
        cout << endl;
    }
    return 0;
}