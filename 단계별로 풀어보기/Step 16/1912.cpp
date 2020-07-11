#include <iostream>
using namespace std;

int main() {
    int n;
    int arr[100000];
    int i;
    int sum = 0;
    int maxNum = -1000;

    cin >> n;
    for(i=0; i<n; i++) {
        cin >> arr[i];
    }

    for(i=0; i<n; i++) {
        sum = max(sum+arr[i], arr[i]);
        maxNum = max(sum, maxNum);
    }
    cout << maxNum << endl;
    return 0;
}