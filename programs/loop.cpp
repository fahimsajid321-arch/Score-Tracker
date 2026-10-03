#include<iostream>
using namespace std;
int main()
{
	int a;
	int prod;
	cout<<"Enter a number:";
	cin>>a;
	for(int b=1;b<=10;b++)
		{
		prod=a*b;
		cout<<a<<"x"<<b<<"="<<prod;
		cout<<endl;
		}
	return 0;
}
