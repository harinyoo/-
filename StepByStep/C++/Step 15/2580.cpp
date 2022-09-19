#include <iostream>
#include <vector>
using namespace std;

int puzzle[9][9];
vector<pair<int, int>> vec;

bool isPromising(int row, int col){
    int i, j;

    for(j=0; j<9; j++) {
        if(j==col) continue;
        if(puzzle[row][col]==puzzle[row][j]) return false;
    }

    for(i=0; i<9; i++) {
        if(i==row) continue;
        if(puzzle[row][col]==puzzle[i][col]) return false;
    }

    for(i=row/3*3; i<row/3*3+3; i++) {
        for(j=col/3*3; j<col/3*3+3; j++) {
            if(i==row && j==col) continue;
            if(puzzle[row][col]==puzzle[i][j]) return false;
        }
    }

    return true;
}

void print() {
    int i, j;

    for(i=0; i<9; i++) {
        for(j=0; j<9; j++) {
            printf("%d ", puzzle[i][j]);
        }
        puts("");
    }
}

void sudoku(int idx) {
    int i;
    int row = vec[idx].first;
    int col = vec[idx].second;

    if(vec.size() <= idx) {
        print();
        exit(0);
    }

    for(i=1; i<=9; i++){
        puzzle[row][col] = i;
        if(isPromising(row, col))
            sudoku(idx+1);
        puzzle[row][col] = 0;
    }
}

int main() {
    int i, j;

    for(i=0; i<9; i++) {
        for(j=0; j<9; j++) {
            scanf("%d", &puzzle[i][j]);
            if(puzzle[i][j]==0) vec.emplace_back(make_pair(i, j));
        }
    }
    sudoku(0);

    return 0;
}