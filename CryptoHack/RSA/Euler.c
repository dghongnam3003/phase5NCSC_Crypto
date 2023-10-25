#include <stdio.h>

long gcd(long long a, long long b){
    if(a == 0) {
        return b;
    } else {
        return gcd(b%a, a);
    }
}

int phi(long long n){
    int result = 1;
    for (int i = 2; i < n; i++) {
        if (gcd(i, n)==1) {
            result += 1;
        }

    return result;
    }
}

int main() {

    printf("%d",phi(2));

    return 0;
}