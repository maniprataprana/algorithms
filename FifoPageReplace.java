// implementation of FIFO Page replacement algorithm
// input : page requests
// outputs :page requests, non page fault requests 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class FifoPageReplace  {
public static void main(String args[])throws IOException   {
		
		/* number of available page frames as command line input , program exits if  wrong arguments*/
		int number_of_available_page_frames = 0;
		int number;
		int page_requests_count=0;
		/* accepts single argument*/
		if (args.length == 1) {
		    try {
		        number_of_available_page_frames = Integer.parseInt(args[0]);
		    } catch (NumberFormatException e) {
		        System.err.println("Argument" + " must be an integer");
		        System.exit(1);
		    }
		}
		else {
			System.err.println("No of arguments  more than one or no argument");
	        System.exit(1);
		}
		/*end of arugument checks , throws NFM exception on invalid argument*/
	
		/*keeps track of the page requests*/	
		ArrayList<Page> pageList = new ArrayList<Page>();
		
		/*input from the user*/
	  	String strInput = ""; 
	 	BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	 	while (true) {
	 		System.out.println("Enter a page number : ");
	 		try{
	 			strInput = reader.readLine(); 
	 			
	 			/*check for EOF*/
		 		if ( strInput == null ) {
		           break;
		         }
	 		}
	 		catch (IOException ioe) {
	 			System.out.println("An unexpected error occured(IO Exception).");
	 		}
	 			 			 			 		
	 		/*check the input and convert it integer format*/
	 		number= isNumeric(strInput);
	 		if (number != -1) {
	 			/*add page to page list*/
	 			Page p = new Page(number);
	 			pageList.add(p);
	 			/*increment page_requests_count by 1 to keep track of requests*/
	 			page_requests_count++;
	 		}
	 		else {
	 			System.out.println("Invalid Input.");
	 		}
		
	 		}
	 	
	 	/*the page requests to this memory are what we make, serves as fifo queue*/
	 	ArrayList<Memory> memList = new ArrayList<Memory>();
	 	
	 	int pageFaults = 0;
	 	int non_page_fault=0;
	 	
	 	for(Page p : pageList) {
	 		if(!p.getActive()) {
				p.setActive();
			}
	 		int found = 0;
	 		if(memList.size() < number_of_available_page_frames) {
	 			/*page already in memory*/
	 			for (Memory m : memList) {
	 				if(m.getPage().getPageNo() == p.getPageNo()) 
	 					{
	 					found = 1;
	 					non_page_fault++;
	 					break;
	 					}
	 			}
	 			if (found == 0) {
	 				memList.add(new Memory(p));
	 				pageFaults++;
	 			}
			} 
	 		else {
	 			
	 			for (Memory m : memList) {
	 				if(m.getPage().getPageNo() == p.getPageNo()) 
	 					{found = 1;non_page_fault++; break;}
	 			}
	 			
	 			if (found == 0) {	 		
	 			/*size of queue full remove the first element*/
	 				memList.remove(0);
	 			 /*add new element at end of queue*/
	 				memList.add(new Memory(p));
	 				pageFaults++;
	 			}
	 			
	 			System.out.println(pageFaults);
	 		}
	 	}
	 	
	 	System.out.println(page_requests_count+" "+(page_requests_count-pageFaults));
	 	
	}
	
	
	
	public static int isNumeric(String number){
	         int isValid = -1;
	         /*Explaination:
	            [0-9]+: Can have any numbers of digits between 0 and 9and more	           
	          */
	         
	          /*remove white spaces from begining*/
	           number=number.replaceAll("^\\s+", "");
	          
	           String str = "";
	           String[] result = number.split(" ");
	           
	           /*assign first token to str and check it for number*/
	           str = result[0];
	           String expression = "^[0-9]+$";
	           CharSequence inputStr = str;
	           Pattern pattern = Pattern.compile(expression);
	           Matcher matcher = pattern.matcher(inputStr);
	           	           
	           if(matcher.find()){
	              isValid = Integer.parseInt(matcher.group(0));
	           }
	           return isValid;
	         }
	

}



class Page {
	private boolean isInMemory = false;
	private int pageNumber;
 
	public Page(int number) {pageNumber = number;}
	public int getPageNo() {
		return pageNumber;
	}
	public void setActive() {isInMemory = true; }
	public boolean getActive() {return isInMemory; }
}



class Memory {
	private Page page ;
 
	public Memory(Page p) {page = p;}
   
	public Page getPage() {return page; }
}
 
