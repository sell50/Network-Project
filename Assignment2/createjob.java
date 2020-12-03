import java.io.IOException;
import java.io.Serializable;
import java.util.*;

/**
 *
 * @author Femi Ayoola
 */

public class createjob implements Serializable
{
    String creator=null;
    String jobname=null;

    public String getJobname() {
        return jobname;
    }

    public void setJobname(String jname) {
        this.jobname = jname;
    }

    public String getCreator() {
        return creator;
    }

    public void setCreator(String creator) {
        this.creator = creator;
    }

    public createjob( String creator, String jobname)
    {
        this.creator = creator;
        this.jobname = jobname;
    }

    @Override
    public String toString() {
        return  "Job creator: " + creator + ", \nJob Name: " + jobname ;
    }

    public static void main(String[] args) throws IOException {

        // create object
        String creat, jobs;
        List<createjob> Job = new ArrayList<>();
        System.out.println("Enetr creator name: ");
        Scanner sc = new Scanner(System.in);
        creat = sc.nextLine();
        System.out.println("Enetr job name: ");
        jobs = sc.nextLine();
        Job.add(new createjob(creat,jobs));
        System.out.println( creat + "\n"+ jobs);

    }

}