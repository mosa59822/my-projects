#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;                               // عدد ۳ رقمی می‌گیرد
    int d1 = n % 10;                        // رقم یکان (راست)
    int d2 = (n / 10) % 10;               // رقم دهگان (وسط)
    int d3 = n / 100;                      // رقم صدگان (چپ)
    cout << "Digit: " << d1 << ", Digit: " << d2 << ", Digit: " << d3;
}
