#include <stdio.h>
#include <math.h>

int main() {
    int n, i;
    float x[10], y[10], logy[10];
    float sx = 0, sy = 0, sxy = 0, sx2 = 0;
    float a, b, r;

    printf("Enter the number of points: ");
    scanf("%d", &n);

    printf("Enter the value of x and y: \n");
    for (i = 0; i < n; i++) {
        scanf("%f %f", &x[i], &y[i]);
        logy[i] = log(y[i]); // Taking natural logarithm of y
    }

    for (i = 0; i < n; i++) {
        sx += x[i];
        sy += logy[i]; // Sum of log(y)
        sxy += x[i] * logy[i]; // Sum of x * log(y)
        sx2 += x[i] * x[i]; // Sum of x^2
    }

    // Calculate b and A' (log of A)
    b = ((n * sxy) - (sx * sy)) / ((n * sx2) - (sx * sx));
    r = (sy / n) - (b * sx / n);

    // Convert A' back to A
    a = exp(r);

    printf("Fitted exponential curve: y = %.4f * e^(%.4f * x)\n", a, b);
    getchar();
    getchar();

    return 0;
}

