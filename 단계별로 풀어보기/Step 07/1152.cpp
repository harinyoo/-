#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

#define MAX_SIZE 1000000
int main() {
    char str[MAX_SIZE];
    fgets(str,MAX_SIZE,stdin);

    int cnt = 0;
    for(int i=0; i<strlen(str)-1; i++){
        if(str[i]==' ') cnt++;
    }

    if(str[0]==' ' && str[strlen(str)-2]!=' ') cnt -= 1;
    else if(str[0]!=' ' && str[strlen(str)-2]==' ') cnt -= 1;
    else if(str[0]==' ' && str[strlen(str)-2]==' ') cnt -= 2;

    cout << cnt+1;
    return 0;
}