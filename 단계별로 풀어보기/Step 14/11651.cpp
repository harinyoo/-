#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool asc(pair<int, int> pair1, pair<int, int> pair2) {
    if(pair1.second == pair2.second) return pair1.first < pair2.first;
    return pair1.second < pair2.second;
}

int main() {
    int N, x, y;
    int i;
    vector<pair<int, int>> location;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> x >> y;
        location.emplace_back(make_pair(x, y));
    }

    sort(location.begin(), location.end(), asc);

    for(i=0; i<N; i++) {
        printf("%d %d\n", location[i].first, location[i].second);
    }
    return 0;
}