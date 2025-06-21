#include <stdio.h>
#include <stdlib.h>

#define MOD 1000000007
#define MAX 2000000

long long *fact, *inv_fact;

long long mod_pow(long long base, long long exp) {
    long long result = 1;
    while (exp > 0) {
        if (exp & 1)
            result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

void precompute_factorials(int max) {
    fact = (long long*)malloc((max + 1) * sizeof(long long));
    inv_fact = (long long*)malloc((max + 1) * sizeof(long long));
    fact[0] = 1;
    for (int i = 1; i <= max; i++) {
        fact[i] = (fact[i-1] * i) % MOD;
    }
    inv_fact[max] = mod_pow(fact[max], MOD - 2);
    for (int i = max - 1; i >= 0; i--) {
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r > n) return 0;
    long long res = fact[n];
    res = (res * inv_fact[r]) % MOD;
    res = (res * inv_fact[n - r]) % MOD;
    return res;
}

int main() {
    int t;
    scanf("%d", &t);

    int *m_values = (int*)malloc(t * sizeof(int));
    int *n_values = (int*)malloc(t * sizeof(int));
    int max_sum = 0;

    for (int i = 0; i < t; i++) {
        scanf("%d %d", &m_values[i], &n_values[i]);
        int sum = m_values[i] + n_values[i];
        if (sum > max_sum)
            max_sum = sum;
    }

    precompute_factorials(max_sum);

    for (int i = 0; i < t; i++) {
        int m = m_values[i];
        int n = n_values[i];
        printf("%lld\n", nCr(m + n, m));
    }

    free(m_values);
    free(n_values);
    free(fact);
    free(inv_fact);

    return 0;
}
