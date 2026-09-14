#include<iostream>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b;                                              // دو عدد می‌گیرد
    int mn = (a < b) ? a : b;                                  // عملگر ؟ کوچکتر را انتخاب
    cout << "The Smallest of " << a << " and " << b << " is: " << mn;
}
