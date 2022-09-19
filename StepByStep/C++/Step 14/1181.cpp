#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

bool length(string &str1, string &str2) {
    if(str1.length() == str2.length()) return str1 < str2;
    return str1.length() < str2.length();
}

int main() {
    int N;
    string str;
    int i, j;
    vector<string> vec;

    cin >> N;
    for(i=0; i<N; i++) {
        cin >> str;
        vec.push_back(str);
    }

    sort(vec.begin(), vec.end(), length);

    for(i=0; i<N; i++) {
        j=0;
        while(j<i) {
            if(vec[i] != vec[j]) j++;
            else break;
        }
        if(j==i) printf("%s\n", vec[i].c_str());
    }

    return 0;
}