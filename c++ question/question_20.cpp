#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;                                   // عدد ۴ رقمی می‌گیرد
    int d1 = n / 1000;                          // رقم هزار
    int d2 = (n / 100) % 10;                    // رقم صد
    int d3 = (n / 10) % 10;                     // رقم ده
    int d4 = n % 10;                            // رقم یکان
    cout << "Digit1=" << d1 << ", Digit2=" << d2
         << ", Digit3=" << d3 << ", Digit4=" << d4;
}
