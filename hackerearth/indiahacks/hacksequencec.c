#include<stdio.h>
void main(){
	long int T, x, i, y, output, a[3]={1,1};
	scanf("%ld",&T);
	for(i=0; i<T; i++){
		scanf("%ld",&x);
		if(x==1){
			y=1;
		}
		else if(x==2){
			y=1;
		}
		else{
			for(i=3;i<=x;i++){
				y=2014*a[1]+69*a[0];
				a[2]=y;
				a[0]=a[1];
				a[1]=a[2];
			}
		}
		output = a[1]%(1000000000+7);
		printf("%ld\n", output);
	}
}
