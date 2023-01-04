#include <iostream>
#define SIZE 10

int data[SIZE] = {23, 40, 12, 34, 10, 48, 1, 36, 92, 14};

void insertionSort(int data[])
{
    for(int index = 1 ; index < SIZE ; index++){
        int temp = data[index];
        int prev = index - 1;
        while( (prev >= 0) && (data[prev] > temp) ) {
            data[prev+1] = data[prev];
            prev--;
        }
        data[prev + 1] = temp;
    }
}

int main() {
    for (int i = 0; i < SIZE; i++) {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
    std::cout << std::endl;

    insertionSort(data);

    for (int i = 0; i < SIZE; i++) {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
}