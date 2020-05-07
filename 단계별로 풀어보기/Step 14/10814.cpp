#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool order(pair<int, string> pair1, pair<int, string> pair2) {
    return pair1.first < pair2.first;
}

int main() {
    int N, age;
    string name;
    int i;
    vector<pair<int, string>> member;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> age >> name;
        member.emplace_back(make_pair(age, name));
    }

    stable_sort(member.begin(), member.end(), order);

    for(i=0; i<N; i++) {
        printf("%d %s\n", member[i].first, member[i].second.c_str());
    }
    return 0;
}