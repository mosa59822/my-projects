
#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;                           // عدد ۴ رقمی می‌گیرد
    int d1 = n / 1000;                  // رقم اول
    int d2 = (n / 100) % 10;           // رقم دوم
    int d3 = (n / 10) % 10;            // رقم سوم
    int d4 = n % 10;                   // رقم چهارم
    cout << "Reversed = " << d4 << d3 << d2 << d1; // معکوس چاپ
}
