#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int i, j;
    if(N==1) cout << "* ";
    else if(N>1) {
        if(N%2==0) {
            for(i=0; i<2*N; i+=2) {
                for(j=0; j<N/2; j++) cout << "* ";
                cout << endl << " ";
                for(j=0; j<N/2; j++) cout << "* ";
                cout << endl;
            }
        }
        else if(N%2==1) {
            for(i=0; i<2*N; i+=2) {
                for(j=0; j<N/2+1; j++) cout << "* ";
                cout << endl << " ";
                for(j=0; j<N/2; j++) cout << "* ";
                cout << endl;
            }
        }
    }
    return 0;
}
