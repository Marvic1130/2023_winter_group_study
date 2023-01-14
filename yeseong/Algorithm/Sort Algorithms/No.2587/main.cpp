#include <iostream>
#define SIZE 5

int main() {
    int* arr = new int[SIZE];

    for (int i = 0; i < SIZE; i++) {
        std::cin >> arr[i];
    }
    for(int i = SIZE-1; i > 0; i--){
        for(int j = 0; j < i; j++){
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    int avr, sum = 0;
    for (int i = 0; i < SIZE; i++) {
        sum += arr[i];
    }
    avr = sum/SIZE;
    std::cout << avr <<std::endl;
    std::cout << arr[2] << std::endl;

    delete[] arr;
}
