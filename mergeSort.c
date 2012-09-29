#include <stdio.h>


void merge(int a[],int p, int q, int r){
	int c[10],b[10];
	int i,j,k,l;
	j =0;k=0;
	int n1,n2;
  	n1=q-p+1;
 	n2=r-q;

  for(i=0; i<n1; i++)
    b[i]=a[p+i];
  for(j=0; j<n2; j++)
    c[j]=a[q+j+1];

	b[i] = 9999;
	c[j] = 9999;
	i=j=0;
	for(k=p;k<=r;k++) {
		if (c[i]<=b[j])
		{
			a[k]=c[i];
			i++;
		}
		else {
			a[k] = b[j];
			j++;
		}
	}



}

void mergesort(int a[],int p, int r) {

	if (p < r) {
		int q = (p+r)/2;
		mergesort(a,p,q);
		mergesort(a,q+1,r);
		merge(a,p,q,r);
	}
	
} 

int main(int argc, char const *argv[])
{
	int a[] = {7,6,5,4,3,2,1,0};
	int p =0, r = 7,i;	
	mergesort(a,p,r);

	for (i = 0; i < 8; ++i) {

		printf("%d \n",a[i] );
	}
	return 0;
}