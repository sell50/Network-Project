import java.io.*;
import java.net.*;

public class ServerThread extends Thread 
{
	
	//Needed Objects
	Socket socket;
	BufferedReader inputStream;
	PrintStream outputStream;
	
	//Needed Variables
	String clientMessage;
	int messageCounter;
	
	/*
	 * Name: ServerThread Constructor
	 * Type: Constructor 
	 * Description: This Constructor Takes in a Socket
	 * 				Object and Sets the Global Socket 
	 * 				== to it
	 */
	ServerThread(Socket socket)
	{
		//Setting Global Socket to the Given Socket
		this.socket = socket;
	}
	
	/*
	 * Name: Overload Run Function
	 * Type: Void
	 * Description: ...
	 */
	public void run() 
	{
		try
		{
			//Input Stream To Get Data From The Client
			inputStream = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			
			//Output Stream To Send Data To The Client
			outputStream = new PrintStream(socket.getOutputStream());
			
			clientMessage = inputStream.readLine();
			
			//For Testing 
			//System.out.println(clientMessage);
			
			//For Testing Purposes
			messageCounter = 1;
			
			//Loop Until Keyword Is Found
			while(clientMessage.compareTo("stop")!=0)
			{
				//Send Rebound Message To The Client
				outputStream.println(messageCounter+" "+clientMessage+" Rebounded By Server\n");
				
				//Clear outputStream Buffer
				outputStream.flush();
				
				//Display The Clients Message On Servers End
				System.out.println("Client has sent the message: "+clientMessage);
				
				//Get New Client Message
				clientMessage = inputStream.readLine();
				
				//Increase Message Counter
				messageCounter++;
			}
			
			//Close All Streams
			inputStream.close();
			outputStream.close();
			socket.close();
			
		}
		catch(Exception e) 
		{
			//Printing The Stack Trace For The User
			e.printStackTrace();
			
			//Closing the ServerThread Program
			System.exit(0);
		}
	}
	
}
