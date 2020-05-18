#include <iostream>
#include <vector>

using namespace std;

int N;
int minNum=1000000000, maxNum=-1000000000;
vector<int> num;
vector<int> oper;

void DFS(int result, int idx, int sum, int sub, int mul, int div) {
    if(idx == N) {
        maxNum = max(maxNum, result);
        minNum = min(minNum, result);
        return;
    }

    if(sum!=0){
        DFS(result+num[idx], idx+1, sum-1, sub, mul, div);
    }
    if(sub!=0){
        DFS(result-num[idx], idx+1, sum, sub-1, mul, div);
    }
    if(mul!=0){
        DFS(result*num[idx], idx+1, sum, sub, mul-1, div);
    }
    if(div!=0){
        DFS(result/num[idx], idx+1, sum, sub, mul, div-1);
    }
}

int main() {
    int i, tmp;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> tmp;
        num.push_back(tmp);
    }
    for(i=0; i<4; i++) {
        cin >> tmp;
        oper.push_back(tmp);
    }

    DFS(num[0], 1, oper[0], oper[1], oper[2], oper[3]);

    cout << maxNum << endl << minNum;
    return 0;
}