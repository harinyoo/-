#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, time;
    vector<int> vec;
    int i;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> time;
        vec.push_back(time);
    }

    sort(vec.begin(), vec.end());
    int sum = vec[0];

    for(i=1; i<N; i++) {
        vec[i] += vec[i-1];
        sum += vec[i];
    }

    cout << sum << endl;
    return 0;
}