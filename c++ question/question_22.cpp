#include<iostream>
#include<string>
using namespace std;
int main(){
    string s;
    getline(cin, s);                        // کل جمله با فاصله می‌گیرد
    cout << "Your feedback: " << s;         // چاپ با پیشوند
}
