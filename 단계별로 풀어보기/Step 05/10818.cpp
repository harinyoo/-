//10818 최소, 최대       -- 시간초과
#include <iostream>
using namespace std;

int main() {
    int size, num;
    int min, max;
    cin >> size;
    int *array = new int[size];

    for(int i=0; i<size; i++){
        cin >> num;
        array[i] = num;
    }

    min = array[0];
    max = array[0];

    for(int j=0; j<size; j++) {
        if(min > array[j]) min = array[j];
        if(max < array[j]) max = array[j];
    }

    cout << min << " " << max;
    return 0;
}