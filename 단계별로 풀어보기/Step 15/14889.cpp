#include <iostream>
#include <vector>

using namespace std;

#define MAX 21

int N;
int skill[MAX][MAX];
bool visited[MAX];
int minNum = 99;

void DFS(int player, int cnt) {
    if(cnt==N/2) {
        vector<int> start, link;
        int startSkills = 0, linkSkills = 0;

        for(int i=1; i<N+1; i++) {
            if(visited[i]) start.push_back(i);
            else link.push_back(i);
        }
        for(int i=0; i<cnt-1; i++) {
            for(int j=i+1; j<cnt; j++) {
                startSkills += (skill[start[i]][start[j]]+skill[start[j]][start[i]]);
                linkSkills += (skill[link[i]][link[j]]+skill[link[j]][link[i]]);
            }
        }
        minNum = min(minNum, abs(startSkills-linkSkills));
        return;
    }

    for(int i=player+1; i<N; i++) {
        if(!visited[i]) {
            visited[i] = true;
            DFS(i, cnt+1);
            visited[i] = false;
        }
    }
}

int main() {
    cin >> N;

    for(int i=1; i<N+1; i++) {
        for(int j=1; j<N+1; j++) {
            scanf("%d", &skill[i][j]);
        }
    }

    DFS(0, 0);
    cout << minNum;
    return 0;
}