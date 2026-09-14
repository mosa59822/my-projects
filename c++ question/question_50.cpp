#include<iostream>
#include<string>
using namespace std;
int main(){
    string user, pass;
    cin >> user >> pass;                                        // نام و رمز می‌گیرد
    if(user == "admin" && pass == "1234")                       // هر دو درست باشند
        cout << "Login successful";
    else
        cout << "Login failed";
}
