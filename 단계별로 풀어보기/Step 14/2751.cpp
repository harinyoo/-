#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, num;
    int i;
    vector<int> vec;
    scanf("%d", &N);

    for(i=0; i<N; i++) {
        scanf("%d", &num);
        vec.push_back(num);
    }

    sort(vec.begin(), vec.end());
    for(i=0; i<N; i++) {
        printf("%d\n", vec[i]);
    }
    return 0;
}


