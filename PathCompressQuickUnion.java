// order n + mln*(n) implementation of qucik find using weights of trees
// impovement upon QuickFindWeight

public class PathCompressQuickUnion {
	private int[] id;
	private int[] sz;

	public PathCompressQuickUnion(int N) {
		id = new int[N];
		sz = new int[N];
		//default initialization
		for(int i=0 ; i<N ; i++) {
			id[i] = i;
			sz[i] = 1;
		}
	}

	//check for connected components
	public boolean connected(int p, int q) {
		return (root(p) == root(q));
	}	

	//find the root node 
	private int root(int p) {
		while(p != id[p]) {
			id[p] = id[id[p]];
			p = id[p];
		}
		return p;
	}

	//union of nodes
	public void union(int p,int q) {
		int i = root(p);
		int j = root(q);
		if (sz[i] < sz[j]) {
			id[i] = j;
			sz[j] = sz[j] + sz[i];
		}
		else {
			id[j] = i;
			sz[i] = sz[i] + sz[i];
		}
	}

	//print function
	void print() {
		for (int i = 0; i < id.length ; i++ ) {
			System.out.print("	"+id[i]);
		} 
		System.out.println();
	}

	public static void main(String []args) {
		PathCompressQuickUnion q = new PathCompressQuickUnion(10);
		q.print();
		q.union(1,2);
		q.union(2,6);
		q.union(7,2);
		q.print();
	}
}