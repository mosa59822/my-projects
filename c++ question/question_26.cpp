#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;                                               // عدد می‌گیرد
    if(n >= 10 && n <= 20) cout << n << " is in range [10,20]"; // بررسی بازه
    else cout << n << " is out of range";
}
