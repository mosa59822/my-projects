#include<iostream>
using namespace std;
int main(){
    int n;
    cin >> n;                        // تعداد جملات می‌گیرد
    double sum = 0;
    for(int i = 1; i <= n; i++)
        sum += 1.0 / i;              // هر جمله = ۱ تقسیم بر i
    cout << "Sum of series = " << sum;
}
