#include<iostream>
using namespace std;
int main(){
    int a=10, b=5, c=2;
    cout << "Without parentheses: " << a / b * c;   // اول تقسیم بعد ضرب
    cout << ", With parentheses: " << a / (b * c);  // اول پرانتز
}
