#include <iostream>
#include <math.h>  

using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    int length, times;
    int l, r;
    cin>>length>>times;
    int *arr = new int[length];

    for (int elem = 0; elem < length; elem++) {
        cin>>arr[elem];
        }
    for (int elem = 0; elem < length; elem++) cout<<arr[elem];
    return 0;
    }