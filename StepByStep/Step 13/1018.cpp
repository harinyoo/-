#include <iostream>
#include <vector>
using namespace std;

vector<string> color;
const string B_board[8] = {"BWBWBWBW",
                           "WBWBWBWB",
                           "BWBWBWBW",
                           "WBWBWBWB",
                           "BWBWBWBW",
                           "WBWBWBWB",
                           "BWBWBWBW",
                           "WBWBWBWB"};
const string W_board[8] = {"WBWBWBWB",
                           "BWBWBWBW",
                           "WBWBWBWB",
                           "BWBWBWBW",
                           "WBWBWBWB",
                           "BWBWBWBW",
                           "WBWBWBWB",
                           "BWBWBWBW"};

int compare(int x, int y) {
    int b_cnt=0, w_cnt=0;
    int i, j;

    for(i=0; i<8; i++) {
        for(j=0; j<8; j++) {
            if(color[x+i][y+j]==B_board[i][j]) b_cnt++;
            if(color[x+i][y+j]==W_board[i][j]) w_cnt++;
        }
    }

    if(b_cnt<=w_cnt) return b_cnt;
    else return w_cnt;
}

int main() {
    int N, M;
    int i, j, cnt=64;
    string str;

    cin >> N >> M;
    for(i=0; i<N; i++) {
        cin >> str;
        color.push_back(str);
    }

    for(i=0; i+7<N; i++) {
        for(j=0; j+7<M; j++) {
            if(cnt >= compare(i, j)) cnt = compare(i, j);
        }
    }

    cout << cnt;
    return 0;
}