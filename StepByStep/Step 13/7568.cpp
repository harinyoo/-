#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, x, y;
    int i, j;
    vector<pair<int, int>> info;
    vector<int> rank;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> x >> y;
        info.push_back(make_pair(x,y));
        rank.push_back(0);
    }

    for(i=0; i<N; i++) {
        for(j=0; j<N; j++) {
            if(info[i].first<info[j].first && info[i].second<info[j].second) {
                rank[i]++;
            }
        }
    }

    for(i=0; i<N; i++) cout << rank[i]+1 << " ";
    return 0;
}