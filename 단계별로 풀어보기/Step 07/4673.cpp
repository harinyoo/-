#include <iostream>
using namespace std;

int d_func(int n) {
    int y = 0;
    int result = n;
    while(n != 0){
        y = n%10;
        result += y;
        n /= 10;
    }
    return result;
}

int main() {
    int self_num[10000];
    int i;
    for(i=0; i<10000; i++) self_num[i] = 1;
    for(i=0; i<10000; i++) {
        int tmp = i+1;
        while(d_func(tmp) <= 10000) {
            self_num[d_func(tmp)-1] = 0;
            tmp = d_func(tmp);
        }
    }

    for(i=0; i<10000; i++) {
        if(self_num[i]!=0) cout << i+1 << endl;
    }
    return 0;
}