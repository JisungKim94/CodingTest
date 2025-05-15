#include <vector>
#include <iostream>

template <typename T>
void print_vector(const std::vector<T>& vec, const std::string& sep = " ") {
    for (const auto& val : vec) {
        std::cout << val << sep;
    }
    std::cout << '\n';
}


template <typename T>
void print_2d_vector(const std::vector<std::vector<T>>& mat, const std::string& sep = " ") {
    for (const auto& row : mat) {
        print_vector(row, sep);
    }
}
