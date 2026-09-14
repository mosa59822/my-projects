#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;                                           // عدد می‌گیرد
    if(n % 5 == 0) cout << "Divisible by 5";            // اگر باقیمانده ۰ بود
    else cout << "Not divisible by 5";
}
