#include <iostream>
using namespace std;

int han(int n) {
    int cnt = 0;
    int diff_1 = 0;
    int diff_2 = 0;
    if(n>=100 && n<=1000) {
        for(int i=100; i<=n; i++) {
            diff_1 = i/100 - (i%100)/10;
            diff_2 = (i%100)/10 - (i%100)%10;
                
            if(diff_1 == diff_2) cnt++;
        }
        cnt += 99;
    }
    else if(n<100) cnt += n;
    
    return cnt;
}

int main() {
    int n;
    cin >> n;
    cout << han(n);
    return 0;
}
