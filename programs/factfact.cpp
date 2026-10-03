#include<iostream>
using namespace std;

double factorialN(int n) {
	double fact=1;
	
	for(double i=1;i<=n;i++)
	fact*=i;
	return fact;
}
int main()
{
	cout<<"Factorial is"<<factorialN(10)<<endl;

}
