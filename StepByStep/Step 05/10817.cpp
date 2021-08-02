#include <iostream>
using namespace std;

int main() {
    int num[3];
    int i=0;

    for(i=0; i<3; i++) {
        cin >> num[i];
    }

    int j, tmp;
    for(i=2; i>0; i--){
        for(j=0; j<i; j++) {
            if(num[j] > num[j+1]) {
                tmp = num[j];
                num[j] = num[j+1];
                num[j+1] = tmp;
            }
        }
    }
    cout << num[1];

    return 0;
}