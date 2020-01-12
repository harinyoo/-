#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int *arr = new int [n];
    
    string str;
    cin >> str;
    
    for(int i=0; i<str.length(); i++) {
        arr[i] = str[i]-48;
    }
    
    int sum = 0;
    for(int j=0; j<n; j++) {
        sum += arr[j];
    }
    
    cout << sum;
    delete[] arr;
    return 0;
}
