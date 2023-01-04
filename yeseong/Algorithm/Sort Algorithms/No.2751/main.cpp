#include <iostream>
using namespace std;
int temp[1000000];

void merge(int data[], int first, int mid, int last)
{
//    int* temp = new int[last - first + 1];
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

//    delete[] temp;
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

int main(){
    // 입력 가속
    std::ios_base::sync_with_stdio(false);
    int size;
    cin >> size;
    int data[size];
    for(int i = 0; i < size; i++)
        cin >> data[i];

    mergeSort(data, 0, size-1);

    for(int i = 0; i < size; i++){
        cout << data[i] << "\n"; // 시간을 줄이기위해 std::endl 대신 \n 사용
    }
}