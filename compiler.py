# Open the file in write mode


# Write content to the file
user_request = '''#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}'''
file = open('./execution.cc', 'w')
file.write(user_request)




# Close the file
file.close()