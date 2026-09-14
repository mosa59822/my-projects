#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;                    // عدد می‌گیرد
    string bin = "";
    while(n > 0){
        bin = (char)('0' + n%2) + bin; // باقیمانده بر ۲ = بیت
        n /= 2;                        // تقسیم بر ۲
    }
    cout << "Binary = " << bin;
}
