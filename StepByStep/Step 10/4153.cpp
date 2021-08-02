#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
    int length[3];
    while(cin >> length[0] >> length[1] >> length[2]){
        if(length[0]==0 || length[1]==0 || length[2]==0) break;
        else{
            sort(length, length+3);
            if(pow(length[2],2) == pow(length[0],2)+pow(length[1],2)) cout << "right" << endl;
            else cout << "wrong" << endl;
        }
    }
    return 0;
}