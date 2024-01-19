#include <iostream>
#include <math.h>

int my_power(int a, int b)
{
    return pow(a, b);
}

float my_log(int a)
{
    return log(a);
}

int main()
{
    int a, b;
    std::cout << "Enter number ";
    std::cin >> a;
    std::cout << "\nEnter power ";
    std::cin >> b;
    std::cout << a << " in power of " << b << " is " << my_power(a, b) << std::endl;
    std::cout << "Sqrt of " << a << " in power of " << b << " is " << my_log(a) << std::endl;

    return 0;
}