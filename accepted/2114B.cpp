#include <iostream>
#include <vector>   

using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(nullptr);

    unsigned short int T;
    cin >> T;
    for (unsigned short int t; t < T; t++) {
        unsigned int N, K;
        cin >> N >> K;
       
        string str;
        cin >> str;
        
        unsigned short int zeros = 0;
        unsigned short int ones = 0;
        for (char ch : str) {
            if (ch == '1') ones++;
            else zeros++;
        }
        
        unsigned short int pairs = 0;
        if (N % 2 == 1) {
            if (ones > zeros) ones -= 1;
            else zeros -= 1;
            pairs += 1;
        }
        
        while (pairs < K) {
            if (ones > zeros) ones -= 2;
            else zeros -= 2;
            pairs += 1;
        }
        
        if (zeros != ones) cout << "NO" << '\n';
        else cout << "YES" << '\n';
    }

    return 0;
}