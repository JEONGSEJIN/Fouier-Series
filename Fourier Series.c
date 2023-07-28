#include <stdio.h>
#include <math.h>
void main()
{
	double n;
	printf("n의 개수:");
	scanf("%f", &n);
	double function=1.5;
	double pi;
	double x;
	double sum = 1.0;

	for (double i = 1; i < n; i++)
	{
		function = (1.5)*(2 - cos(i*pi) * 2)*sin(i*x);
		sum += function;
	}
	printf("%f", sum);
	return 0;
}
