#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int i;
    string ans;
    for(i=0; i<N; i++) {
        cin >> ans;
        int tmp = 0;
        int score = 0;
        int j;
        for(j=0; j<ans.size(); j++) {
            if(ans[j] == 'O') tmp++;
            else tmp = 0;
            score += tmp;
        }
        cout << score << endl;
    }
    return 0;
}