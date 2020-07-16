import java.util.Arrays;

public class TransitCalculator {

    // Days a person will be using the transit system (max 30 days)
    int daysOfUse;
    // Number of individual rides the person expects to take in that time
    int individualRides;

    // Arrays for fare options and there prices
    String[] fareOptions = {"Pay-per-ride", "7-day Unlimited rides", "30-day Unlimited rides"};
    double[] farePrices = {2.75, 33, 127};

    public TransitCalculator(int rides, int days){
        daysOfUse = days;
        individualRides = rides;
    }

    // Return price/ride on 7-day Unlimited rides fare
    public double unlimited7Price() {
        int weeks = daysOfUse / 7;

        double totalFare;

        if (daysOfUse % 7 == 0) {
            totalFare = weeks * farePrices[1];
        } else {
            totalFare = (weeks + 1) * farePrices[1];
        }

        return totalFare / individualRides;
    }

    // Return price/ride on 30-day Unlimited rides fare
    public double unlimited30Price() {
        int weeks = daysOfUse / 30;

        double totalFare;

        if (daysOfUse % 30 == 0) {
            totalFare = weeks * farePrices[2];
        } else {
            totalFare = (weeks + 1) * farePrices[2];
        }

        return totalFare / individualRides;
    }

    // Return array of doubles of price/ride for each fare option
    public double[] getRidePrices() {

        double[] fares = new double[3];

        double payPerRideFare = farePrices[0];
        double unlimited7DaysFare = unlimited7Price();
        double unlimited30DaysFare = unlimited30Price();

        fares[0] = payPerRideFare;
        fares[1] = unlimited7DaysFare;
        fares[2] = unlimited30DaysFare;

        return fares;
    }

    // Return a advice to pick the best fare for rides/days
    public String getBestFare(){
        double[] arrayPrices = getRidePrices();
        double lowestPrice = arrayPrices[0];
        int index = 0;

        for(int i=0; i<3; i++){
            if(arrayPrices[i] < lowestPrice){
                lowestPrice = arrayPrices[i];
                index = i;
            }
        }

        // Format lowestPrice to print
        lowestPrice = Math.round(lowestPrice * 100.0) / 100.0;

        return "You should get the " + fareOptions[index] + " option at $" + lowestPrice + " per ride.";
    }

    public String toString(){
        return "Vai da o cu " + daysOfUse + " horas";
    }

    public static void main(String[] args){

        TransitCalculator object = new TransitCalculator(54, 26);
        System.out.println(object.getBestFare());
    }
}
