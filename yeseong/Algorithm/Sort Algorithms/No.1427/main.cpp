#include <iostream>
using namespace std;

void sort(int arr[], int n){
    for(int i = n-1; i > 0; i--){
        for(int j = 0; j < i; j++){
            if(arr[j] < arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int input;
    cin >> input;
    int* data = new int[10];
    for (int i = 0; i < 10; i++) {
        data[i] = -1;
    }

    int count = 0;

    while (input){
        data[count++] = input%10;
        input /= 10;
    }
    sort(data, count);
    for (int i = 0; i < count; i++) {
        cout << data[i];
    }

}
