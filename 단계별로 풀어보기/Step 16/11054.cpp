#include <iostream>
using namespace std;

int main() {
    int n, length=0;
    int arr[1000];
    int dp_1[1000];
    int dp_2[1000];
    int length_1[1000];
    int length_2[1000];
    int i, j;
    int longest = 0;

    cin >> n;
    for(i=0; i<n; i++) {
        cin >> arr[i];
    }

    dp_1[0] = arr[0];
    length_1[0] = 1;
    for(i=1; i<n; i++) {
        if(dp_1[length] < arr[i])
            dp_1[++length] = arr[i];
        else {
            for(j=0; j<=length; j++) {
                if(arr[i] <= dp_1[j]) {
                    dp_1[j] = arr[i];
                    break;
                }
            }
        }
        length_1[i] = length+1;
    }

    length = 0;
    dp_2[0] = arr[n-1];
    length_2[n-1] = 1;
    for(i=n-2; i>-1; i--) {
        if(dp_2[length] < arr[i])
            dp_2[++length] = arr[i];
        else {
            for(j=0; j<=length; j++) {
                if(arr[i] <= dp_2[j]) {
                    dp_2[j] = arr[i];
                    break;
                }
            }
        }
        length_2[i] = length+1;
    }

    for(i=0; i<n; i++) {
        if(longest < length_1[i]+length_2[i])
            longest = length_1[i]+length_2[i]-1;
    }
    cout << longest << endl;
    return 0;
}