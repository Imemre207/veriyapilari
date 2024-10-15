#include<stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>





// Rastgele tam sayılardan oluşan dizi oluşturma fonksiyonu
void generate_random_array(int *arr, int length) {
    for (int i = 0; i < length; i++) {
        arr[i] = rand() % 100 + 1;
    }
}

// Zaman ölçüm fonksiyonu
double measure_time(void (*algorithm)(int*, int), int *arr, int size) {
    clock_t start, end;
    start = clock();
    algorithm(arr, size);
    end = clock();
    return ((double) (end - start)) / CLOCKS_PER_SEC;
}


void fonksiyon1(int *arr, int n) {
    int toplam = 0;
    
    // O(N) işlemi
    for (int i = 0; i < n; i++) {
        toplam += arr[i] * arr[i];
    }

    // O(N^2) işlemi
    for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
            toplam = toplam + 1;
        }
    }
}

void basamak_toplami(int *arr, int n)
{
    int toplam=0;
    while(n>0)
    {
        int basamak =n%10;
        toplam+=basamak;
        n=n/10;
    }
}


int main()
{

    srand(time(NULL));  // Rastgele sayı üreteci için seed
    int sizes[] = {1, 10, 100, 1000, 10000, 100000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);
    
    printf("Size\tFonksiyon1\tBasamak Toplamı\n");
    for (int i = 0; i < num_sizes; i++) {
        int size = sizes[i];
        int *arr = (int*)malloc(size * sizeof(int));

        generate_random_array(arr, size);
        double fonk_time = measure_time(fonksiyon1, arr, size);

        generate_random_array(arr, size);
        double bas_time = measure_time(basamak_toplami, arr, size);

        printf("%d\t%.6f\t%.6f\n", size, fonk_time,bas_time);

        free(arr);
    }
    return 0;
}

