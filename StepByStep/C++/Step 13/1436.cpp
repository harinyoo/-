#include <iostream>
using namespace std;

int main() {
    string sss = "666";
    string str;
    int N, i, cnt=0;
    int num = 666;

    cin >> N;
    while(cnt!=N){
        str = to_string(num);
        for(i=0; i+2<str.size(); i++) {
            if(str[i]==sss[0] && str[i+1]==sss[1] && str[i+2]==sss[2]) {
                cnt++;
                break;
            }
        }
        num++;
    }

    cout << num-1;
    return 0;
}