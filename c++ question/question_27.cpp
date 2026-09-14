#include<iostream>
using namespace std;
int main(){
    int a, b, c;
    cin >> a >> b >> c;                              // سه عدد می‌گیرد
    int mx = a;                                      // فرض اولی بزرگترین
    if(b > mx) mx = b;                               // با b مقایسه
    if(c > mx) mx = c;                               // با c مقایسه
    cout << "Largest = " << mx;
}
