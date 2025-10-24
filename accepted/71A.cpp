#include <iostream>

using namespace std;

int main() {
    unsigned char n;
    scanf("%hhu", &n);

    for (unsigned char i = 0; i < n; i++) {
        string word;
        cin >> word;

        if (word.length() <= 4) {
            cout << word << '\n';
        } else {
            char sch = word[0];
            char ech = word[word.length()-1];
            printf("%c%d%c\n", sch, word.length()-2, ech);
        }
    }
    

}
