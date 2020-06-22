#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    int i;
    vector<int> vec;

    vec.push_back(0);
    vec.push_back(1);
    vec.push_back(2);

    cin >> N;
    for(i=3; i<=N; i++) {
        vec.push_back((vec[i-2]+vec[i-1])%15746);
    }
    cout << vec[N] << endl;
    return 0;
}