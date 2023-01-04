#include <iostream>
#define SIZE 10

int data[SIZE] = {23, 40, 12, 34, 10, 48, 1, 36, 92, 14};

void _quickSort(int data[], int start, int end){
    if(start >= end){
        return;
    }

    int pivot = start;
    int i = pivot + 1;
    int j = end;
    int temp;

    while(i <= j){
        while(i <= end && data[i] <= data[pivot]){
            i++;
        }
        while(j > start && data[j] >= data[pivot]){
            j--;
        }

        if(i > j){
            temp = data[j];
            data[j] = data[pivot];
            data[pivot] = temp;
        }else{
            temp = data[i];
            data[i] = data[j];
            data[j] = temp;
        }
    }

    // 분할 계산
    _quickSort(data, start, j - 1);
    _quickSort(data, j + 1, end);
}

void quickSort(int data[]){
    _quickSort(data, 0, SIZE-1);
}

int main() {
    for (int i = 0; i < SIZE; i++) {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
    std::cout << std::endl;

    quickSort(data);

    for (int i = 0; i < SIZE; i++) {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
}