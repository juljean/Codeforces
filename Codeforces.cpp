#include <iostream>
#include <vector>
#include <math.h>  

using namespace std;

int query(int *arr, int l, int r, int par, int **lookup){
    // 0 - min
    int j = (int)(log2(r - l + 1));
    if (par == 0){
        if (arr[lookup[l][j]] <=
                arr[lookup[r - (1 << j) + 1][j]])
            return arr[lookup[l][j]];
        else
            return arr[lookup[r - (1 << j) + 1][j]];
    }
 
    else {
        if (arr[lookup[l][j]] >=
                arr[lookup[r - (1 << j) + 1][j]])
            return arr[lookup[l][j]];
        else
            return arr[lookup[r - (1 << j) + 1][j]];
    }
    return 0;
}

void preprocess(int *arr, int n, int **lookup_min, int **lookup_max) {
    int j = 1;
    while ((1 << j) <= n){
        int i = 0;
        while (i + (1 << j) - 1 < n){
            if (arr[lookup_min[i][j - 1]] < arr[lookup_min[i + (1 << (j - 1))][j - 1]])
                lookup_min[i][j] = lookup_min[i][j - 1];
            else lookup_min[i][j] = lookup_min[i + (1 << (j - 1))][j - 1];
 
            if (arr[lookup_max[i][j - 1]] > arr[lookup_max[i + (1 << (j - 1))][j - 1]])
                lookup_max[i][j] = lookup_max[i][j - 1];
            else
                lookup_max[i][j] = lookup_max[i + (1 << (j - 1))][j - 1];
            i += 1;
        }
        j += 1;
    }
}

void calculate(int *arr, int l, int r, int **lookup_min, int **lookup_max, int length){
    int counter = 0;
    int l_new, r_new;
    while (1){
        if (l == 0 && r == length){
            cout << counter << endl;
            break;
        }
 
        l_new = query(arr, l, r, 0, lookup_min);
        r_new = query(arr, l, r, 1, lookup_max);
 
        if (l == r || (l == l_new-- && r == r_new--)){
            cout << -1 << endl;
            break;   
        }
 
        l = l_new - 1;
        r = r_new - 1;
 
        counter++;
    }
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    
    int length, times;
    cin>>length>>times;

    int *arr = new int[length];
    for (int elem = 0; elem < length; elem++) cin>>arr[elem];

    int sparse_matrix_length = ceil(log2(length)) + 1;
    int **lookup_min, **lookup_max;
    lookup_min = new int*[length];
    lookup_max = new int*[length];

    for(int i = 0; i < length; i++){
        lookup_min[i] = new int[sparse_matrix_length];
        lookup_max[i] =  new int[sparse_matrix_length];
        for(int j = 0; j < sparse_matrix_length; j++){
            if (j==0){
                lookup_min[i][j] = i;
                lookup_max[i][j] = i;
            } 
            else {
                lookup_min[i][j] = 0;
                lookup_max[i][j] = 0;
            }
        } 
    }

    preprocess(arr, length, lookup_min, lookup_max);
    // for(int i = 0; i < length; i++){
    //     for(int j = 0; j < sparse_matrix_length; j++) cout<<lookup_max[i][j]<<endl;
    //     cout<<endl;
    // }

    int l, r;
    for (int t = 0; t < times; t++){
        cin>>l>>r;
        calculate(arr, l - 1, r - 1, lookup_min, lookup_max, length - 1);
    }
}
