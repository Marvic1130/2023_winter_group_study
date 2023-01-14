#include <iostream>
#define SIZE 10001

using namespace std;

int main() {
    int *incount = new int[SIZE];

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        incount[num]++;
    }
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < incount[i]; j++) {
            cout << i << "\n";
        }
    }
}
