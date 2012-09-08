//easy implementation of Quick find union operation
//while doing algo course on coursera
//o(n^2)

public class QuickFindUF {
	
	private int[] id;

	public QuickFindUF(int N) {
		id = new int[N];
		//default set each object to itself
		for (int i=0; i<N ; i++) {
			id[i] =i;
		}
	}	
	public boolean connected(int p,int q)	{
		return (id[p] == id[q] );
	}


	public void union(int p,int q) {
		int pid = id[p];
		int qid = id[q]; 
		for (int i = 0; i < id.length ; i++ ) {
			if (id[i] == pid) {
				id[i] = qid;
			} 
		}
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