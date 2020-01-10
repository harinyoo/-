#include <iostream>
using namespace std;

int main() {
    int test;
    scanf("%d", &test);

    int a, b;
    for(int i=0; i<test; i++) {
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }
    return 0;
}