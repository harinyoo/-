#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool asc(pair<int, int> a, pair<int, int> b) {
    if(a.second==b.second)
        return a.first < b.first;
    return a.second < b.second;
}

int main() {
    int N, s, e;
    vector<pair <int, int>> info;
    int i;
    int cnt = 1;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> s >> e;
        info.emplace_back(make_pair(s, e));
    }
    sort(info.begin(), info.end(), asc);
    int endTime = info[0].second;

    for(i=1; i<N; i++) {
        if(endTime <= info[i].first) {
            cnt++;
            endTime = info[i].second;
        }
    }
    cout << cnt << endl;
    return 0;
}