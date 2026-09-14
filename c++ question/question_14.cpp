#include<iostream>
using namespace std;
int main(){
    int a, b, c;
    cin >> a >> b >> c;          // سه عدد می‌گیرد
    if(a < b) swap(a, b);        // بزرگترین به a می‌رود
    if(a < c) swap(a, c);        // دوباره مقایسه
    if(b < c) swap(b, c);        // b و c مقایسه می‌شوند
    cout << "Sorted: " << a << " " << b << " " << c;
}
