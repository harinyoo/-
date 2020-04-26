//2562 최댓값
#include <iostream>
using namespace std;

int main() {
    int array[9];
    int num, max, idx;
    for(int i=0; i<9; i++) {
        cin >> num;
        array[i] = num;
    }
    max = array[0];

    for(int i=0; i<9; i++) {
        if(max <= array[i]) {
            max = array[i];
            idx = i+1;
        }
    }
    cout << max << endl << idx;
    return 0;
}
