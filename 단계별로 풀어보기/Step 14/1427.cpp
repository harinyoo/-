#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool desc(int a, int b) {
    return a > b;
}

int main() {
    string str;
    int i;
    vector<int> vec;

    cin >> str;
    for(i=0; i<str.length(); i++) {
        vec.push_back(str[i]-'0');
    }

    sort(vec.begin(), vec.end(), desc);

    for(i=0; i<vec.size(); i++) cout << vec[i];
    return 0;
}