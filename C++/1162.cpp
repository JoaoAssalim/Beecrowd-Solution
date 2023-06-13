#include <iostream>
using namespace std;

int merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1];
    int R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];

    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0;
    int j = 0;
    int k = l;
    int count = 0;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
            count += n1 - i;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }

    return count;
}

int mergeSort(int arr[], int l, int r) {
    int count = 0;
    if (l < r) {
        int m = l + (r - l) / 2;
        count += mergeSort(arr, l, m);
        count += mergeSort(arr, m + 1, r);
        count += merge(arr, l, m, r);
    }
    return count;
}

int main() {
    int n; cin >> n;
    for(int i = 0; i < n; i++){
        int x; cin >> x;
        int arr[x];
        for (int i = 0; i < x; i++) {
            cin >> arr[i];
        }
        int count = mergeSort(arr, 0, x - 1);
        cout << "Optimal train swapping takes " << count << " swaps." << endl;
    }
}
