// Author: Hoai Dinh

#pragma once

#define SWAP(x, y) {int temp = x; x = y; y = temp;}

void merge_sort(int array[], int left, int right);

void insertion_sort(int array[], int size);
void selection_sort(int array[], int size);
void bubble_sort(int array[], int size);