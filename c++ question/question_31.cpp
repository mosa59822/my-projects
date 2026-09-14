#include<iostream>
using namespace std;
int main(){
    int a, b, c;
    cin >> a >> b >> c;                                 // سه عدد می‌گیرد
    int mx = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c); // ؟ تودرتو
    cout << "Largest = " << mx;
}
