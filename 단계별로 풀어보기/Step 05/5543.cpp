#include <iostream>
using namespace std;

int main() {
    int burgerPrice[3];
    int setBurger=2000;
    int beveragePrice[2];
    int setBeverage=2000;

    int i;
    for(i=0; i<3; i++) {
        cin >> burgerPrice[i];
        if(setBurger > burgerPrice[i]) setBurger = burgerPrice[i];
    }
    for(i=0; i<2; i++) {
        cin >> beveragePrice[i];
        if(setBeverage > beveragePrice[i]) setBeverage = beveragePrice[i];
    }

    cout << setBurger+setBeverage-50;
    return 0;
}