#include <iostream>
using namespace std;

void star(int i, int j, int n){
    if(i%3==1 && j%3==1) cout << " ";
    else {
        if(n/3<=i<n/3*2 && n/3<=j<n/3*2) star(i/3, j/3, n/3);
        else cout << "*";
    }
}

int main() {
    int N;
    cin >> N;

    int i, j;
    for(i=0; i<N; i++) {
        for(j=0; j<N; j++) {
            star(i,j,N);
        }
        cout << endl;
    }
    return 0;
}