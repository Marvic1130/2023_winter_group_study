#include <iostream>

int main() {
    int n[3], i, j, temp;

    for(i = 0; i < 3; i++){
        std::cin >> n[i];
    }

    for(i = 1; i < 3; i++){
        for(j = 0; j < 3 - i; j++){
            if(n[j] > n[j+1]){
                temp = n[j+1];
                n[j+1] = n[j];
                n[j] = temp;
            }
        }
    }
    std::cout << n[1] << std::endl;
}
