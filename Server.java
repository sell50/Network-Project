import java.io.*;
import java.net.*;

public class Server 
{
	//Needed Objects
	Socket socket;
	ServerSocket serverSocket;
	ServerThread serverThread;		//Constructed Class Object
	
	/*
	 * Name: Server Constructor
	 * Type: Constructor 
	 * Description: Basic Constructor
	 */
	Server() throws Exception
	{
		//Make Connection
		SCC();
	}
	
	/*
	 * Name: Server to Client Connection Function
	 * Type: Void
	 * Description: This function will wait for the client to 
	 * 				send a message wanting to connect with the 
	 * 				server. After the connection is established
	 * 				a new server thread is created to allow other
	 * 				clients to connect at the same time.
	 */
	public void SCC() throws Exception
	{
		//Message to show Server is running
		System.out.println("Server is waiting for Connection...");
		
		//Initializing The Server Socket Object
		serverSocket = new ServerSocket(4446);
		
		//Loop Forever Until Program Is Terminated
		while(true)
		{
			try
			{
				//Creating Socket Object to Connect to Client
				socket = serverSocket.accept();
				
				//Displaying That The Connection Was Made
				System.out.println("Connection Made With Client");
				
				//Initializing The ServerThread Object
				serverThread = new ServerThread(socket);
				
				//Starting The Thread When a New Client Connects
				serverThread.start();
			}
			catch(Exception e)
			{
				//Print Error
				e.printStackTrace();
				
				//Display To User That The Connection Has Failed
				System.out.println("Connection Error ... Exiting Program ");
				
				//Closing the Server Program
				System.exit(0);
			}
		}
	}
	
	/*
	 * Name: Main
	 * Type: Static Void
	 * Description: Creates Server Object
	 */
	public static void main(String Args[]) throws Exception
	{
		Server mainServer = new Server();
	}
}
