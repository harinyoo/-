#include <iostream>
using namespace std;

int d_func(int n) {
        if (n < 10) {
            n = n+n;
        }
        else if(n>=10 && n<100) {
            n = n + (n/10) + (n%10);
        }
        else if(n>=100 && n<1000) {
            n = n + (n/100) + ((n%100)/10) + ((n%100)%10);
        }
        else if(n>=1000 && n<10000){
            n = n + (n/1000) + ((n%1000)/100) + (((n%1000)%100)/10) + (((n%1000)%100)%10);
        }
        else if(n==10000) n = 10001;

        return n;
}

int main() {
   int arr[10000] = {0};
   for(int i = 0; i<10000; i++) {
       arr[i] = i+1;
   }
   int num = 0;
   for(int k=1; k<10000; k++) {
       num = d_func(k);
       for (int j = 0; j < 10000; j++) {
           if (num == arr[j]) arr[j] = 0;
       }
   }

   for(int l=0; l<10000; l++) {
       if(arr[l] != 0) cout << arr[l] << endl;
   }
    return 0;
}