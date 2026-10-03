#include<iostream>
using namespace std;
int main()
{
	int seconds;
	cout<<"Enter Seconds:";
	cin>>seconds;
	int minutes=seconds/60;
	int remainingSeconds=seconds%60;
	cout<<minutes<<" Minutes and "<<remainingSeconds<<" Seconds";
	return 0;
}
