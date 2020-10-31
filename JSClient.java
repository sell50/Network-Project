import java.io.*;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Femi Ayoola
 */

public class JSClient
{
    private String serverName = "localhost";
    private int serverPort = 4446;
    private Socket socket = null;
    BufferedReader inputStream;			//Input: Server--> Client
    BufferedReader inputStream2;		//Input: User ---> Client

    DataOutputStream outputStream;		//Output: Client--> Server

    //Needed Variables
    String clientMessage;
    String serverResponse;

    public JSClient() throws Exception
    {
        //Make Connection
        CSC();

        //Send Messages Client<-->Server
        JSClient();
    }

    public void CSC() throws Exception
    {
        try
        {
            //Creating Socket Object to Connect to Server
            socket = new Socket("localhost",serverPort);
            System.out.println("Connected to server " + socket.getRemoteSocketAddress());

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

    public void JSClient()
    {
        //Prompting The User To Enter A String Message, Telling The User That 'stop' Is The Key Word To Shutdown The Connection
        System.out.println("Enter 'client' to view list of job or 'stop' to break the connection");

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

                    try (ObjectInputStream objectInputStream = new ObjectInputStream(socket.getInputStream())) {
                        Object object = objectInputStream.readObject();

                        List<createjob> Job = (List<createjob>) object;
                        for (int i = 0; i < Job.size(); i++) {
                            System.out.println(Job.get(i));
                        }
                    }
                    //socket.close();
            catch (IOException | ClassNotFoundException e) {
                    System.out.println("Error : " + e.getMessage());
                }
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

        }
    }

    public static void main(String[] args) throws Exception {
        JSClient JcClient = new JSClient();
    }
}
