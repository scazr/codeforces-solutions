#include <cstdio>

int main() {
    unsigned char w;
    scanf("%hhu", &w);
    
    if (w <= 3 || w % 2) { printf("NO\n"); return 0; }
    printf("YES\n");

    return 0;
}