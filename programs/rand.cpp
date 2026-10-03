 #include<iostream>
 #include<cstdlib>
 using namespace std;
 int main()
 {
	int n1=0,n2=0,sum=0,ans=0;
	n1=rand()%2;
	n2=rand()%2;
	sum=n1+n2;
	cout<<"Answer is:";
	cin>>ans;
	if(sum==ans)
		cout<<"Correct";
	else
		cout<<"incorrect";
	return 0;
}
