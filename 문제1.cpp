#include <stdio.h>
#pragma warning (disable: 4996)

int main() {
	int n, i, j;
	int	num[1000];
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%d", &num[i]);
	}

	for (i = 0; i < n; i++) {
		for (j = 1; j < n - i; j++) {
			if (num[j - 1] > num[j]) {
				int temp = num[j - 1];
				num[j - 1] = num[j];
				num[j] = temp;
			}
		}
	}

	for (i = 0; i < n; i++) {
		printf("%d\n", num[i]);
	}

	return 0;

}