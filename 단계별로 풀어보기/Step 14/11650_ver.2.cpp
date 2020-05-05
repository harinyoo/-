#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void sorting(vector<pair<int, int>> &vec) {
    int i, j;
    pair<int, int> tmp;

    for(i=0; i<vec.size()-1; i++) {
        for(j=0; j<vec.size()-1-i; j++) {
            if(vec[j].first > vec[j+1].first) {
                tmp = vec[j];
                vec[j] = vec[j+1];
                vec[j+1] = tmp;
            }

            else if(vec[j].first == vec[j+1].first) {
                if(vec[j].second > vec[j+1].second) {
                    tmp = vec[j];
                    vec[j] = vec[j+1];
                    vec[j+1] = tmp;
                }
            }
        }
    }
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

    sorting(location);

    for(i=0; i<N; i++) {
        printf("%d %d\n", location[i].first, location[i].second);
    }
    return 0;
}