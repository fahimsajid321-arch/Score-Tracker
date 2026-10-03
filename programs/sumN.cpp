#include<iostream>
using namespace std;

int sumN(int n) {
	int sum=0;
	for(int i=0;i<=n;i++)
		sum+=i;
		return sum;
}
int main()
{
	cout<<"Sum is "<<sumN(5)<<endl;
	cout<<"Second is "<<sumN(80);
}
