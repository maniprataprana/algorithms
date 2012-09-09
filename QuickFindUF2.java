//easy implementation of Quick find union operation
//while doing algo course on coursera
//o(n)

public class QuickFindUF2 {
	
	private int[] id;

	public QuickFindUF2(int N) {
		id = new int[N];
		//default set each object to itself
		for (int i=0; i<N ; i++) {
			id[i] =i;
		}
	}	
	public boolean connected(int p,int q)	{
		return (root(p) == root(q) );
	}

	private int root(int i) {
		while(i != id[i]) {
			i = id[i];
		}
		return i;
	}
	public void union(int p,int q) {
		int i = root(p);
		int j = root(q); 
		id[i] = j;
	}

	void print() {
		for (int i = 0; i < id.length ; i++ ) {
			System.out.print("	"+id[i]);
			} 
			System.out.println();
		}
	
	public static void main(String []args) {
		QuickFindUF q = new QuickFindUF(10);
		q.print();
		q.union(1,2);
		q.union(2,6);
		q.union(7,2);
		q.print();
	}
}