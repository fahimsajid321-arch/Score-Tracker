#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int tiution;
	string living;
	string instate="Instate";
	string outstate="Outstate";
	cout<<"you are from:";
	cin>>living;
	if(living==instate)
		tiution=5000;
	else
		tiution=15000;
	cout<<"The tiution is:"<<tiution;
	return 0;
}
	

