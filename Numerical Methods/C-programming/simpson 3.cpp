#include <stdio.h>

#include <math.h>

#define f(x) (sin(x))

int main() {
    int n, i;
    float x0, x1, h, term = 0, v;

    printf("Enter Lower and Upper Limit (in radians): \n");
    scanf("%f %f", &x0, &x1);

    printf("Enter number of intervals (multiple of 3): \n");
    scanf("%d", &n);

    h = (x1 - x0) / n;

    term = f(x0) + f(x1);

    for (i = 1; i < n; i++) {
        float x = x0 + i * h;
        if (i % 3 == 0)
            term += 2 * f(x);
        else
            term += 3 * f(x);
    }

    v = (3 * h / 8) * term;

    printf("Value of Integration: %f\n", v);

  	getchar();
   getchar();
    return 0;
}

