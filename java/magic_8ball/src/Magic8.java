import java.util.Random;

public class Magic8 {
    public static void main(String[] args){

        // Draws a number between 0:19
        Random rand = new Random();
        int rand_value = rand.nextInt(20);

        System.out.println("Think your yes/no question to get an answer.");
        System.out.println();

        // Wait 5 seconds
        try { Thread.sleep (5000); } catch (InterruptedException ex) {}

        // Commom switch case
        switch (rand_value){
            case 0:
                System.out.println("It is certain."); break;
            case 1:
                System.out.println("It is decidedly so."); break;
            case 2:
                System.out.println("Without a doubt."); break;
            case 3:
                System.out.println("Yes - definitely."); break;
            case 4:
                System.out.println("You may rely on it."); break;
            case 5:
                System.out.println("As I see it, yes."); break;
            case 6:
                System.out.println("Most likely"); break;
            case 7:
                System.out.println("Outlook good."); break;
            case 8:
                System.out.println("Yes."); break;
            case 9:
                System.out.println("Signs point to yes."); break;
            case 10:
                System.out.println("Reply hazy, try again."); break;
            case 11:
                System.out.println("Ask again later."); break;
            case 12:
                System.out.println("Better not tell you now."); break;
            case 13:
                System.out.println("Cannot predict now."); break;
            case 14:
                System.out.println("concentrate and ask again."); break;
            case 15:
                System.out.println("Don't count on it."); break;
            case 16:
                System.out.println("My reply is no."); break;
            case 17:
                System.out.println("My sources say no."); break;
            case 18:
                System.out.println("Outlook not so good."); break;
            case 19:
                System.out.println("Very doubtful."); break;
            default:
                System.out.println("Keep thinking about this question.");
        }

        /*
        New switch case on Java SE 14 released on March 17, 2020

        switch (rand_value) {
            case 0 -> System.out.println("It is certain.");
            case 1 -> System.out.println("It is decidedly so.");
            case 2 -> System.out.println("Without a doubt.");
            case 3 -> System.out.println("Yes - definitely.");
            case 4 -> System.out.println("You may rely on it.");
            case 5 -> System.out.println("As I see it, yes.");
            case 6 -> System.out.println("Most likely");
            case 7 -> System.out.println("Outlook good.");
            case 8 -> System.out.println("Yes.");
            case 9 -> System.out.println("Signs point to yes.");
            case 10 -> System.out.println("Reply hazy, try again.");
            case 11 -> System.out.println("Ask again later.");
            case 12 -> System.out.println("Better not tell you now.");
            case 13 -> System.out.println("Cannot predict now.");
            case 14 -> System.out.println("concentrate and ask again.");
            case 15 -> System.out.println("Don't count on it.");
            case 16 -> System.out.println("My reply is no.");
            case 17 -> System.out.println("My sources say no.");
            case 18 -> System.out.println("Outlook not so good.");
            case 19 -> System.out.println("Very doubtful.");
            default -> System.out.println("Keep thinking about this question.");
        }
         */

    }
}
