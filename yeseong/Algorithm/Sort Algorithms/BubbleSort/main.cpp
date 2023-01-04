#include <iostream>
#define SIZE 10

int data[SIZE] = {23, 40, 12, 34, 10, 48, 1, 36, 92, 14};

void bubbleSort(int data[]){
    int temp;
    for(int i = 0; i < SIZE; i++){
        for (int j = 1; j < SIZE-i; j++) {
            if(data[j-1] > data[j]){
                temp = data[j-1];
                data[j-1] = data[j];
                data[j] = temp;
            }
        }
    }
}

int main() {
    for (int i = 0; i < SIZE; i++) {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
    std::cout << std::endl;

    bubbleSort(data);

    for (int i = 0; i < SIZE; i++) {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
}
