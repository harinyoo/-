//2920 음계
#include <iostream>
using namespace std;

int main() {
    int array[8];
    int num;
    int cnt1=0, cnt2=0;
    for(int i=0; i<8; i++) {
        cin >> num;
        array[i] = num;
    }
    for(int j=0; j<7; j++) {
        if(array[j]<array[j+1]) cnt1++;
        else cnt2++;
    }
    if(cnt1==7) cout << "ascending";
    else if(cnt2==7) cout << "descending";
    else cout << "mixed";

    return 0;
}
