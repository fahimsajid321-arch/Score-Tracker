#include<iostream>
using namespace std;

int factorialN(int n) {
	int fact=1;
	
	for(int i;i<=n;i++)
	fact*=i;
	return fact;
}
int main()
{
	cout<<"Factorial is "<<factorialN(5)<<endl;
	cout<<"Factorial is "<<factorialN(5);
}
