#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int t;
    scanf("%d\n", &t);

    unsigned long long total = 0;
    char num[60];
    for (int i = 0; i < t; i++) {
        fgets(num, sizeof(num), stdin);
        char first15[16] = {0};
        strncpy(first15, num, 15);
        unsigned long long val = strtoull(first15, NULL, 10);
        total += val;
    }

    char total_str[30];
    sprintf(total_str, "%llu", total);

    for (int i = 0; i < 10 && total_str[i] != '\0'; i++) {
        putchar(total_str[i]);
    }
    putchar('\n');
    return 0;
}
