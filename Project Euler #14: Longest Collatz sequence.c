#include <stdio.h>
#include <stdlib.h>

#define MAX_N 5000000 

unsigned int *cache;
unsigned int *result;

unsigned int collatz_length(unsigned long long n, unsigned int *cache) {
    if (n < MAX_N && cache[n] != 0)
        return cache[n];
    unsigned int length;
    if (n % 2 == 0) {
        length = 1 + collatz_length(n / 2, cache);
    } else {
        length = 1 + collatz_length(3 * n + 1, cache);
    }
    if (n < MAX_N)
        cache[n] = length;
    return length;
}

int main() {
    int t;
    scanf("%d", &t);
    int *tests = (int *)malloc(t * sizeof(int));
    int max_n = 0;
    for (int i = 0; i < t; i++) {
        scanf("%d", &tests[i]);
        if (tests[i] > max_n)
            max_n = tests[i];
    }

    cache = (unsigned int *)calloc(MAX_N, sizeof(unsigned int));
    result = (unsigned int *)malloc((max_n + 1) * sizeof(unsigned int));
    cache[1] = 1;

    unsigned int max_length = 1;
    unsigned int max_num = 1;

    for (unsigned int i = 1; i <= (unsigned int)max_n; i++) {
        unsigned int length = collatz_length(i, cache);
        if (length >= max_length) {
            max_length = length;
            max_num = i;
        }
        result[i] = max_num;
    }

    for (int i = 0; i < t; i++) {
        printf("%u\n", result[tests[i]]);
    }

    free(cache);
    free(result);
    free(tests);

    return 0;
}
