import java.util.Arrays;

public class TransitCalculator {

    // Days a person will be using the transit system (max 30 days)
    int daysOfUse;
    // Number of individual rides the person expects to take in that time
    int individualRides;

    // Arrays for fare options and there prices
    String[] fareOptions = {"Pay-per-ride", "7-day Unlimited rides", "30-day Unlimited rides"};
    double[] farePrices = {2.75, 33, 127};

    public TransitCalculator(int days, int rides){
        daysOfUse = days;
        individualRides = rides;
    }

    public double unlimited7Price(int days, int rides) {
        int weeks = days / 7;

        double totalFare;

        if (days % 7 == 0) {
            totalFare = weeks * farePrices[1];
        } else {
            totalFare = (weeks + 1) * farePrices[1];
        }

        return totalFare / rides;
    }


    public String toString(){
        return "Vai da o cu " + daysOfUse + " horas";
    }

    public static void main(String[] args){


        TransitCalculator object = new TransitCalculator(30, 50);
        System.out.println(object.unlimited7Price(6, 14));
    }
}
