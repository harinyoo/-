#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int i, num;
    int cnt = 0;
    for(i=0; i<N; i++) {
        cin >> num;
        if(num==2) cnt++;
        else if(num>2){
            int j;
            for(j=2; j<num; j++) {
                if(num%j == 0) break;
            }
            if(j==num) cnt++;
        }
    }

    cout << cnt;
    return 0;
}