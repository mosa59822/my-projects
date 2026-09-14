#include<iostream>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b;                                      // دو عدد می‌گیرد
    cout << a << "& " << b << " = " << (a & b);         // AND بیتی
    cout << ", " << a << "| " << b << " = " << (a | b); // OR بیتی
}
