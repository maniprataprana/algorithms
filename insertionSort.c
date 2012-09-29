#include <stdio.h>
#include <string.h>


int main(int argc, char args[]) {
	int a[] = {5,2,4,6,1,3	};
	int i,j;
	int count = sizeof(a)/sizeof(int);
	int key;

	for(i = 1;i<count;i++){
		key = a[i];
		j = i - 1; 
		while(j >= 0 && a[j] > key){
			a[j+1] = a[j];
			j--;
		}
		a[j+1] = key;
	}
	for (i = 0; i <count; ++i)
	{
		printf("%d\n",a[i]);
	}
	return 0;
}
