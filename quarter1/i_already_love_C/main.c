#include <stdio.h>

/**
 * main - prints Hello PLD !
 *
 * Return: always return 0
 *
 * a: first integer to be multiplied
 * b: second integer to be multiplied
 *
 * multiply: displays the product of two integers
 *
 **/

void multiply(int a, int b)
{
	int result = a * b;

	printf("%d\n", result);
}

int main(void)
{
	int number;

	printf("Hello PLD !\n");


	for (number = 0; number <= 10; number++)
	{
		printf("Tour %d\n", number);
	}
	while (number <= 20)
	{
		printf("Tour %d\n", number);
		number++;
	}

	multiply(35, 57);

	return (0);

}
