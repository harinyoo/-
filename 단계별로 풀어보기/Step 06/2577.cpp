#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    int array7[7], array8[8], array9[9];
    int cnt_arr[10] = {0};

    cin >> a >> b >> c;
    int result = a*b*c;

    if(result<=9999999) {
        int div = 1000000;
        for(int i=0; i<7; i++) {
            array7[i] = result / div;
            result = result - array7[i]*div;
            div = div/10;

            for(int x=0; x<10; x++) {
                if(array7[i] == x) cnt_arr[x]++;
            }
        }


    }
    else if(result>10000000 && result<=99999999) {
        int div = 10000000;
        for(int j=0; j<8; j++) {
            array8[j] = result / div;
            result = result - array8[j]*div;
            div = div/10;

            for(int x=0; x<10; x++) {
                if(array8[j] == x) cnt_arr[x]++;
            }
        }
    }
    else if(result>100000000) {
        int div = 100000000;
        for(int k=0; k<9; k++) {
            array9[k] = result / div;
            result = result - array9[k]*div;
            div = div/10;

            for(int x=0; x<10; x++) {
                if(array9[k] == x) cnt_arr[x]++;
            }
        }
    }

    for(int l=0; l<10; l++) {
        cout << cnt_arr[l] << endl;
    };
    return 0;
}
