#include <chrono>
#include <iostream>
#include <sstream>

#include "sorts.hpp"

std::string print_array(int array[], int size) {
    std::stringstream ss;

    ss << "{";
    for(int i = 0; i < size; i++) {
        ss << " " << array[i] << ((i != size-1) ? ", " : "");
    }
    ss << "}";

    return ss.str();
}

int main() {

    int array[] = {5, 2, 4, 7, 1, 3, 2, 6};
    int size = 8;

    std::cout << "Array: " << print_array(array, size) << std::endl;
    std::cout << "Running Merge Sort" << std::endl;
    merge_sort(array, 0, size-1);
    std::cout << "Array after Merge Sort: " << print_array(array, size) << std::endl;


    return 0;
}