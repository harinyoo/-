#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

vector<int> vec;
int i;

void mean() {
    double sum = 0;
    for(i=0; i<vec.size(); i++) sum += vec[i];
    cout << round(sum/vec.size()) << endl;
}

void median() {
    cout << vec[vec.size()/2] << endl;
}

void mode() {
    int cnt[8001];
    vector<int> temp;

    fill_n(cnt, 8001, 0);

    for(i=0; i<vec.size(); i++) {
        cnt[vec[i]-vec[0]]++;
    }

    int max = cnt[0];
    for(i=0; i<8001; i++) {
        if(max < cnt[i]) max = cnt[i];
    }

    for(i=0; i<8001; i++) {
        if(max==cnt[i]) temp.push_back(i);
    }

    if(temp.size()==1) cout << temp[0]+vec[0] << endl;
    else cout << temp[1]+vec[0] << endl;
}

void range() {
    cout << vec[vec.size()-1]-vec[0] << endl;
}

int main() {
    int N, num;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> num;
        vec.push_back(num);
    }
    sort(vec.begin(), vec.end());

    mean();
    median();
    mode();
    range();

    return 0;
}