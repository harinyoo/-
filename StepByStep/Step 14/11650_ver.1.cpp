#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, x, y;
    int i;
    vector<pair<int, int>> location;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> x >> y;
        location.emplace_back(make_pair(x, y));
    }

    sort(location.begin(), location.end());

    for(i=0; i<N; i++) {
        printf("%d %d\n", location[i].first, location[i].second);
    }
    return 0;
}