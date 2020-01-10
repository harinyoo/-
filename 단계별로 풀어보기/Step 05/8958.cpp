#include <iostream>
#include <string>
#include <string.h>
using namespace std;

int main() {
    int size = 0;
    cin >> size;
    string str;
    int score = 0;
    int *result = new int[size];

    for (int i = 0; i < size; i++) {
        result[i] = 0;
        score = 0;
        cin >> str;
        for (int j = 0; j < str.size(); j++) {
            if (str[j] == 'O') score++;
            else score = 0;
            result[i] += score;
        }
    }
    for (int k = 0; k < size; k++) {
        cout << result[k] << endl;
    }
    return 0;
}