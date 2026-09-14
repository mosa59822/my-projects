#include<iostream>
#include<cmath>
using namespace std;
int main(){
    double deg;
    cin >> deg;                                             // درجه می‌گیرد
    double rad = deg * 3.14159 / 180;                       // تبدیل به رادیان
    cout << "sin(" << deg << ") = " << sin(rad);            // محاسبه sin
}
