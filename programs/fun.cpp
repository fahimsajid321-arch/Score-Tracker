#include<iostream>
using namespace std;

int sum(int a,int b) {
	int s=a+b;
	cout<<"Sum is equals to ";
	return s;
}
int minOfTwo(int a,int b){

	if(a<b)
	 cout<<"Minimum number is: ";
	else
	 cout<<"Minimum number is: ";
}
int main()
{
	cout<<sum(15,35)<<endl;
	cout<<sum(23,25)<<endl;
	cout<<minOfTwo(5,15);
}
