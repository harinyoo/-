#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> vec;
    int num, i;
    for(i=0; i<N; i++) {
        cin >> num;
        vec.push_back(num);
    }

    int sum = 0;
    int j, k, tmp;
    for(i=0; i<N-2; i++) {
        for(j=i+1; j<N-1; j++) {
            for(k=j+1; k<N; k++) {
                if(sum<=vec[i]+vec[j]+vec[k] && vec[i]+vec[j]+vec[k]<=M)
                    sum = vec[i]+vec[j]+vec[k];
            }
        }
    }
    cout << sum;
    return 0;
}