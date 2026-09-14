#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;                                    // عدد می‌گیرد
    if(n % 2 == 0) cout << n << " is even";      // اگر باقیمانده ۰ بود زوج
    else cout << n << " is odd";                 // وگرنه فرد
}
