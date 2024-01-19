#include <iostream>
#include <math.h>

int my_power(int a, int b)
{
    return pow(a, b);
}

int main()
{
    int a, b;
    std::cout << "Enter number ";
    std::cin >> a;
    std::cout << "\nEnter power ";
    std::cin >> b;
    std::cout << a << " in power of " << b << " is " << my_power(a, b) << std::endl;
    return 0;
}