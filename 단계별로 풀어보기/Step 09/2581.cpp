#include <iostream>
#include <vector>
using namespace std;

int main() {
    int M, N;
    cin >> M >> N;

    int i, sum=0;
    vector<int> vec;
    for(i=M; i<=N; i++) {
        if(i==2) {
            vec.push_back(i);
            sum += i;
        }
        else if(i>2) {
            int j=2;
            for(; j<i; j++) {
                if(i%j == 0) break;
            }
            if(j==i)  {
                vec.push_back(i);
                sum += i;
            }
        }
    }

    if(sum==0) cout << "-1";
    else cout << sum << endl << vec.at(0);
    return 0;
}