#include <iostream>
#define SIZE 10

int data[SIZE] = {23, 40, 12, 34, 10, 48, 1, 36, 92, 14};

void merge(int data[], int first, int mid, int last)
{
    int* temp = new int[last - first + 1];
    int i, j, k;
    i = first;
    j = mid + 1;
    k = 0;

    while (i <= mid && j <= last)
    {
        if (data[i] <= data[j])
            temp[k++] = data[i++];
        else
            temp[k++] = data[j++];
    }

    if (i > mid) {
        while (j <= last) {
            temp[k++] = data[j++]; 
        }
    }
    else {
        while (i <= mid) {
            temp[k++] = data[i++];
        }
    }
    for (i = first, k = 0; i <= last; i++, k++) {
        data[i] = temp[k];
    }

    delete[] temp;
}

void mergeSort(int arr[], int first, int last)
{
    if (first < last)
    {
        int mid = (first + last) / 2;
        mergeSort(arr, first, mid);
        mergeSort(arr, mid + 1, last);
        merge(arr, first, mid, last);
    }
}

int main() {
    for (int i = 0; i < SIZE; i++) {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
    std::cout << std::endl;

    mergeSort(data, 0, SIZE-1);

    for (int i = 0; i < SIZE; i++) {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
}
