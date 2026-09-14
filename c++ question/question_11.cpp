#include<iostream>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b;                                    // دو عدد می‌گیرد
    cout << (a > b ? "true" : "false");               // مقایسه می‌کند
    cout << ", Squares: " << a*a << " and " << b*b;   // توان ۲ هر دو
}
