#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, a_num, b_num;
    vector<pair <int, int>> vec;
    int dp[100];
    int length = 0;
    int i, j;

    cin >> n;
    for(i=0; i<n; i++) {
        cin >> a_num >> b_num;
        vec.emplace_back(make_pair(a_num, b_num));
    }

    sort(vec.begin(), vec.end());

    dp[0] = vec[0].second;
    for(i=1; i<n; i++) {
        if(dp[length] < vec[i].second)
            dp[++length] = vec[i].second;
        else {
            for(j=0; j<=length; j++) {
                if(vec[i].second <= dp[j]) {
                    dp[j] = vec[i].second;
                    break;
                }
            }
        }
    }

    cout << n-length-1 << endl;
    return 0;
}