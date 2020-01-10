#include <iostream>
using namespace std;

bool han(int n) {
    int a, b, c;
    a = n/100;
    b = (n%100)/10;
    c = (n%100)%10;
    if((a-b)==(b-c)) return true;
    else return false;
}

int main() {
    int arr[901] = {0};
    for(int i=0; i<901; i++) {
        arr[i] = i+100;
    }
    int n;
    cin >> n;
    int cnt=0;
    if(n>=100) {
        for(int j=0; j<n-100+1; j++) {
            if(han(arr[j])) cnt++;
        }
        cnt += 99;
    }
    else if(n<100) cnt = n;
    cout << cnt;

    return 0;
}
