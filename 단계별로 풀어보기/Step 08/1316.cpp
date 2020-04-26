#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    string str;
    int arr[26];
    int j, cnt = 0;
    for(int i=0; i<N; i++) {
        cin >> str;
        fill_n(arr, 26, 0);
        arr[str[0]-'a'] = 1;
        for(j=1; j<str.length(); j++) {
            if(str[j-1] != str[j]) {
                int idx = str[j]-'a';
                if(arr[idx] == 0) arr[idx]++;
                else break;
            }
        }
        if(j==str.length()) cnt++;
    }
    cout << cnt;

    return 0;
}