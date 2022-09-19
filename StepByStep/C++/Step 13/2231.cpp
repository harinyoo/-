#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int i;
    int sum, tmp;
    for(i=1; i<N+1; i++) {
        tmp = i;
        sum = i;
        while(tmp!=0) {
            sum += tmp%10;
            tmp /= 10;
        }
        if(sum==N){
            cout << i;
            return 0;
        }
    }

    cout << 0;
    return 0;
}