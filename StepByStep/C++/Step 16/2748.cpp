#include <iostream>
#include <vector>
using namespace std;

vector<long> vec;

int main() {
    int N, i;

    vec.push_back(0);
    vec.push_back(1);

    cin >> N;
    for(i=2; i<=N; i++) {
        vec.push_back(vec[i-1]+vec[i-2]);
    }

    cout << vec[N] << endl;
    return 0;
}