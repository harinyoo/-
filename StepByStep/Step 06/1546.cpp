#include <iostream>
using namespace std;

int main() {
    int size;
    float max;

    cin >> size;
    float *arr = new float[size];

    for(int i=0; i<size; i++) {
        cin >> arr[i];
    }

    max = arr[0];
    for(int j=0; j<size; j++) {
        if(max < arr[j]) max = arr[j];
    }

    for(int k=0; k<size; k++) {
        arr[k] = arr[k]/max*100;
    }

    float sum = 0;
    for(int l=0; l<size; l++) {
        sum += arr[l];
    }
    float avg = sum/size;
    cout << avg;

    return 0;
}
