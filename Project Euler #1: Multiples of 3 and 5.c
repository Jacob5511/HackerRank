#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        int n,res =0 ; 
        scanf("%d",&n);
        for (int i = 0; i < n; i++)
        {
            if (i % 5 == 0 || i % 3 == 0)
                res += i;
        }
        printf("%d\n", res);
    }
    return 0;
}
