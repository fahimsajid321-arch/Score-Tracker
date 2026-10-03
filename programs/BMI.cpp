 #include<iostream>
 using namespace std;
 int main()
 {
 	float BMI;
 	cout<<"Enter Your BMI:";
 	cin>>BMI;
 	if(BMI<18.5)
 		cout<<"Under Weight";
 	else if(BMI<25.0)
 		cout<<"Normal";
 	else if(BMI<30.0)
 		cout<<"Over weight";
 	else
 		cout<<"Obese";
	return 0;
 }
