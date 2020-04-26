#include <iostream>
using namespace std;

int main() {
    int C;
    cin >> C;

    int i;
    for(i=0; i<C; i++) {
        int N;
        cin >> N;
        int *score = new int[N];
        int j;
        int sum = 0;
        float avg;
        for(j=0; j<N; j++) {
            cin >> score[j];
            sum += score[j];
        }
        avg = (float)sum/N;
        int cnt = 0;
        for(j=0; j<N; j++) {
            if (score[j] > avg) cnt++;
        }
        cout << fixed;
        cout.precision(3);
        cout << (float)cnt/N*100 << "%" << endl;
    }
    return 0;
}

