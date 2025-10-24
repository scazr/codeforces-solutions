#include <iostream>
#include <cstdint>
#include <algorithm>

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(nullptr);

    uint16_t N;
    std::cin >> N;
    
    int16_t X = 0;
    for (uint16_t n = 0; n < N; n++) {
        std::string opx;
        std::cin >> opx;
        uint8_t op = opx[0] != 'X' ? opx[0] : opx[2]; 
        switch (op) {
            case '+':
            X++;
            break;
            case '-':
            X--;    
            break;
        }
    }
    std::cout << X;

    return 0;
}