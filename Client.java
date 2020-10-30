import java.io.*;
import java.net.*;

public class Client 
{

	//Needed Objects
	Socket socket;
	BufferedReader inputStream;			//Input: Server--> Client
	BufferedReader inputStream2;		//Input: User ---> Client
	
	DataOutputStream outputStream;		//Output: Client--> Server
	
	//Needed Variables
	String clientMessage;
	String serverResponse;
	
	
	/*
	 * Name: Constructor
	 * Type: Void
	 * Description: This constructor will run functions which will
	 * 				connect and allow messages to be sent back and 
	 * 				fourth between the Client and Server
	 */
	Client() throws Exception
	{
		//Make Connection
		CSC();
		
		//Send Messages Client<-->Server
		CSM();
	}
	
	/*
	 * Name: Client to Server Connection Function
	 * Type: Void
	 * Description:This function will look for the Server to 
	 * 				send a message wanting to connect. 
	 * 				After the connection is established
	 * 				the Client can now send messages to the Server
	 */
	public void CSC() throws Exception
	{
		try
		{
			//Creating Socket Object to Connect to Server
			socket = new Socket("localhost",4446);
			
			//Input Stream To Get Data From The Server
			inputStream = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			
			//Input Stream To Get Data From The Client User
			inputStream2 = new BufferedReader(new InputStreamReader(System.in));
			
			//Output Stream To Send Data To The Server
			outputStream = new DataOutputStream(socket.getOutputStream());
		}
		catch(Exception e) 
		{
			//Print Error
			e.printStackTrace();
			
			//Display To User That The Connection Has Failed
			System.out.println("Connection Error ... Exiting");
			
			//Closing the Client Program
			System.exit(0);
		}	
	}
	
	/*
	 * Name: Client to Server Message Function
	 * Type: Void
	 * Description: This Function Lets The User of The Client Program 
	 * 				To Send String Messages To The Server As Well 
	 * 				Get The Rebounded Message That The Server Sends Back
	 */
	public void CSM()
	{
		//Prompting The User To Enter A String Message
		System.out.println("What String Would You Like To Send To The Server");
		
		//Telling The User That 'stop' Is The Key Word To Shutdown The Connection
		System.out.println("Enter 'stop' To Break The Connection With The Server");
	
		try
		{
			//Getting Client Message From User
			clientMessage = inputStream2.readLine();
			
			//Looping Until Keyword Is Typed
			while(clientMessage.compareTo("stop")!=0)
			{
				//Sending The Client Message Via Bytes
				outputStream.writeBytes(clientMessage+"\n");
				
				//Clearing Out The Buffer From Next Message
				outputStream.flush();
				
				//Obtaining The Servers Response Message
				serverResponse = inputStream.readLine();
				
				//Printing The Server Message To The Client 
				System.out.println("Server Response: "+serverResponse);
				
				//Getting Client Message From User
				clientMessage = inputStream2.readLine();
			}
			
			//Closing All Open Streams
			inputStream.close();
			inputStream2.close();
			outputStream.close();
			socket.close();
			
			//Displaying That The Connection Has Been Closed To The Client
			System.out.println("Connection Has Been Closed");
		}
		catch(Exception e)
		{
			//Printing The Stack Trace For The User
			e.printStackTrace();
			
			//Closing the Client Program
			System.exit(0);
		}
	}
	
	/*
	 * Name: Main
	 * Type: Static Void
	 * Description: Creates Client Object
	 */
	public static void main(String Args[]) throws Exception
	{
		Client client = new Client();
	}
	
}
