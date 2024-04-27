# Open the file in write mode
file = open('./execution.cc', 'w')

# Write content to the file
user_request = '''#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}'''
file.write(user_request)

# Close the file
file.close()