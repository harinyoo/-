#include <iostream>
using namespace std;

int main(){
    int n,length=0;
    int i, j;
    int A[1000];
    int location[1000];

    cin >> n;
    for(i=0;i<n;i++)
        scanf("%d",&A[i]);

    location[0]=A[0];

    for(i=1; i<n; i++) {
        if(A[i] > location[length])
            location[++length] = A[i];
        else {
            for(j=0; j<=length; j++) {
                if(location[j] >= A[i]) {
                    location[j] = A[i];
                    break;
                }
            }
        }
    }
    cout<<length+1<<endl;
    return 0;
}