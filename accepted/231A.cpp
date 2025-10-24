#include <iostream>
#include <bitset>
#include <algorithm>
#include <cstdint>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(0);

    uint16_t N;
    cin >> N;
    uint16_t total = 0;

    for (uint16_t n = 0; n < N; n++) {
        string STR;
        cin >> ws;
        getline(cin, STR);
        STR.erase(remove(STR.begin(), STR.end(), ' '), STR.end());
        bitset<3> sure{STR};

        if (sure.count() > 1) total++;
    }
    cout << total;
        
    return 0;
}