#include <iostream>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;

    string str;
    cin >> str;

    int arr[N];
    for(int i=0; i<N+1; i++) {
        arr[i] = str[i] - '0';
    }

    int sum = 0;
    for(int i=0; i<N; i++) {
        sum += arr[i];
    }

    cout << sum;

    return 0;
}