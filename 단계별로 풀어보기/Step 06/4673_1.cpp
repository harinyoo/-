#include <iostream>
using namespace std;

int d_fun(int n) {
    int result = n;
    while(n != 0) {
        result += n%10;
        n /= 10;
    }
    return result;
}

int main() {
    int arr[10000];
    for(int i=0; i<10000; i++) {
        arr[i] = i+1;
    }
    for(int j=0; j<10000; j++) {
        for(int k=0; k<10000; k++) {
            if(d_fun(j) == arr[k]) arr[k] = 0;
        }
    }
    for(int l=0; l<10000; l++) {
        if(arr[l] != 0) cout << arr[l] << endl;
    }
    return 0;
}
