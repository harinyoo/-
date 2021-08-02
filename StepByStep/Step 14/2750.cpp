#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    int num, i, j, tmp;
    vector<int> vec;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> num;
        vec.push_back(num);
    }

    for(i=0; i<N*(N-1)/2; i++) {
        for(j=0; j<N-1; j++) {
            if(vec[j] >= vec[j+1]) {
                tmp = vec[j];
                vec[j] = vec[j+1];
                vec[j+1] = tmp;
            }
        }
    }

    for(i=0; i<N; i++){
        cout << vec[i] << endl;
    }
    return 0;
}