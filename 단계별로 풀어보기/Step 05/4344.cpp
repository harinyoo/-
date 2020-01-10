#include <iostream>
using namespace std;

int main() {
    int test;
    cin >> test;
    float *ratio = new float[test];
    for(int i=0; i<test; i++) {
        ratio[i] = 0;
        int student;
        cin >> student;
        int *score = new int[student];
        int sum = 0;
        for(int j=0; j<student; j++) {
            cin >> score[j];
            sum += score[j];
        }
        float average = float(sum)/float(student);
        int cnt = 0;
        for(int k=0; k<student; k++) {
            if(average < score[k]) cnt++;
        }
        ratio[i] = float(cnt)/float(student)*100;
    }
    for(int l=0; l<test; l++) {
        cout << fixed;
        cout.precision(3);
        cout << ratio[l] << "%" << endl;
    }
    return 0;
}

