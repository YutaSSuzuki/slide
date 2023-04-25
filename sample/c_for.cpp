#include <iostream>
#include <chrono>
using namespace std;
int main()
{   int n = 100000000;
    long sum_ = 0;
    auto start = chrono::steady_clock::now(); // 開始時刻
    for (int i = 1; i <= n; i++) {
        sum_ += i;}
    auto end = chrono::steady_clock::now(); // 終了時刻
    auto diff = end - start; // 経過時間
    cout << "Sum = " << sum_ << endl;
    cout << "Elapsed time = " << chrono::duration<double, milli>(diff).count() << " ms" << endl;
    return 0;}
/*C++でのfor文処理時間:0.224624秒*/
