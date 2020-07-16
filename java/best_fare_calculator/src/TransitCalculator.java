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
    public TransitCalculator(int rides, int days, int age){
        daysOfUse = days;
        individualRides = rides;
        userAge = age;
    }

    // Return price/ride on 7-day Unlimited rides fare
    public double unlimited7Price() {
        int weeks = daysOfUse / 7;

        double totalFare;

        if (daysOfUse % 7 == 0) {
            totalFare = (userAge < 65) ? weeks * normalFarePrices[1] : weeks * reducedFarePrices[1];
        } else {
            totalFare = (userAge < 65) ? (weeks+1) * normalFarePrices[1] : (weeks+1) * reducedFarePrices[1];
        }

        return totalFare / individualRides;
    }

    // Return price/ride on 30-day Unlimited rides fare
    public double unlimited30Price() {
        int weeks = daysOfUse / 30;

        double totalFare;

        if (daysOfUse % 30 == 0) {
            totalFare = (userAge < 65) ? weeks * normalFarePrices[2] : weeks * reducedFarePrices[2];
        } else {
            totalFare = (userAge < 65) ? (weeks+1) * normalFarePrices[2] : (weeks+1) * reducedFarePrices[2];
        }

        return totalFare / individualRides;
    }

    // Return array of doubles of price/ride for each fare option
    public double[] getRidePrices() {

        double[] fares = new double[3];

        double payPerRideFare = (userAge < 65) ? normalFarePrices[0] : reducedFarePrices[0];
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

    // Default toString method
    public String toString(){
        return "This user is " + userAge + " years old.";
    }

    public static void main(String[] args){
        TransitCalculator youngBoy = new TransitCalculator(54, 26,20);
        TransitCalculator oldMan = new TransitCalculator(54, 26, 71);

        System.out.println(oldMan);
    }
}
