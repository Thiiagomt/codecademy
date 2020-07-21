import java.util.Arrays;

public class TransitCalculator {

    // Days a person will be using the transit system (max 30 days)
    int daysOfUse;
    // Number of individual rides the person expects to take in that time
    int individualRides;
    // Age of user
    int userAge;

    // Arrays for fare options and there prices
    String[] fareOptions = {"Pay-per-ride", "7-day Unlimited rides", "30-day Unlimited rides"};
    double[] normalFarePrices = {2.75, 33, 127};
    double[] reducedFarePrices = {1.35, 16.5, 63.5};

    // Constructor
    public TransitCalculator(int individualRides, int daysOfUse, int userAge){
        this.daysOfUse = daysOfUse;
        this.individualRides = individualRides;
        this.userAge = userAge;
    }

    // Return price/ride on 7-day Unlimited rides fare
    public double unlimited7Price() {
        int weeks = this.daysOfUse / 7;

        double totalFare;

        if (this.daysOfUse % 7 == 0) {
            totalFare = (this.userAge < 65) ? weeks * this.normalFarePrices[1] : weeks * this.reducedFarePrices[1];
        } else {
            totalFare = (this.userAge < 65) ? (weeks+1) * this.normalFarePrices[1] : (weeks+1) * this.reducedFarePrices[1];
        }

        return totalFare / this.individualRides;
    }

    // Return price/ride on 30-day Unlimited rides fare
    public double unlimited30Price() {
        int weeks = this.daysOfUse / 30;

        double totalFare;

        if (this.daysOfUse % 30 == 0) {
            totalFare = (this.userAge < 65) ? weeks * this.normalFarePrices[2] : weeks * this.reducedFarePrices[2];
        } else {
            totalFare = (this.userAge < 65) ? (weeks+1) * this.normalFarePrices[2] : (weeks+1) * this.reducedFarePrices[2];
        }

        return totalFare / this.individualRides;
    }

    // Return array of doubles of price/ride for each fare option
    public double[] getRidePrices() {

        double[] fares = new double[3];

        double payPerRideFare = (this.userAge < 65) ? this.normalFarePrices[0] : this.reducedFarePrices[0];
        double unlimited7DaysFare = unlimited7Price();
        double unlimited30DaysFare = unlimited30Price();

        double[] prices = {payPerRideFare, unlimited7DaysFare, unlimited30DaysFare};

        int i = 0;
        for(Double fare : prices){
            fares[i] = fare;
            i += 1;
        }

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

        return "You should get the " + this.fareOptions[index] + " option at $" + lowestPrice + " per ride.";
    }

    // Default toString method
    public String toString(){
        return "This user is " + this.userAge + " years old.";
    }

    public static void main(String[] args){
        TransitCalculator youngBoy = new TransitCalculator(54, 26,20);
        TransitCalculator oldMan = new TransitCalculator(54, 26, 71);

        System.out.println(Arrays.toString(oldMan.getRidePrices()));
    }
}
