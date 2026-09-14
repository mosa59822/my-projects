#include<iostream>
#include<string>
using namespace std;
int main(){
    string pass;
    cin >> pass;                                        // رمز می‌گیرد
    if(pass.length() < 8)                               // اگر طول کمتر از ۸ بود
        cout << "Password is too short";
    else
        cout << "Password is OK";
}
