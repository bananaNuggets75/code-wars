#include <cstdint>
#include <string>

std::string add_binary(uint64_t a, uint64_t b) {
    uint64_t sum = a + b; 
    std::string binary = ""; 

    if (sum == 0) return "0";
    while (sum > 0) {
        binary = std::to_string(sum % 2) + binary;  
        sum /= 2; 
    }
    return binary;
}
