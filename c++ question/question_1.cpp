#include<iostream>
#include<string>
using namespace std;
int main(){
    string a, b;
    cin >> a;          // فقط تا اولین فاصله می‌خواند
    getline(cin, b);   // بقیه خط را می‌خواند
    cout << "cin reads: " << a << ", getline reads: " << b;
}
