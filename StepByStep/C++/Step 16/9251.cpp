#include <iostream>
using namespace std;

int main() {
    string str1, str2;
    int cnt [1001][1001];

    cin >> str1 >> str2;
    int len1 = str1.length();
    int len2 = str2.length();
    int i, j;

    for(i=1; i<=len1; i++) {
        for(j=1; j<=len2; j++) {
            if(str1[i-1]==str2[j-1])
                cnt[i][j] = cnt[i-1][j-1] + 1;
            else
                cnt[i][j] = max(cnt[i][j-1], cnt[i-1][j]);
        }
    }

    cout << cnt[len1][len2] << endl;
    return 0;
}