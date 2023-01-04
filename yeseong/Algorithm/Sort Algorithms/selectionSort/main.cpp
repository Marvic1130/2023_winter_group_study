#include <iostream>
#define SIZE 10

int data[SIZE] = {23, 40, 12, 34, 10, 48, 1, 36, 92, 14};

void selectionSort(int data[]) {
    int indexMin, temp;
    for (int i = 0; i < SIZE - 1; i++) {
        indexMin = i;
        for (int j = i + 1; j < SIZE; j++) {
            if (data[j] < data[indexMin]) {
                indexMin = j;
            }
        }
        temp = data[indexMin];
        data[indexMin] = data[i];
        data[i] = temp;
    }
}

int main() {
    for (int i = 0; i < SIZE; i++) {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
    std::cout << std::endl;

    selectionSort(data);

    for (int i = 0; i < SIZE; i++) {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
}
