#include<iostream>
#include<string>
using namespace std;
int main(){
    string s;
    getline(cin, s);                                    // کل جمله را می‌گیرد
    cout << "Number of characters: " << s.length();    // طول رشته = تعداد حروف
}
