// 17. Display Multiples of 5 (Table of 5)
public class MultiplesOfFive {
    public static void displayTableOfFive() {
        System.debug('Table of 5:');
        for (Integer i = 1; i <= 10; i++) {
            Integer result = 5 * i;
            System.debug('5 x ' + i + ' = ' + result);
        }
    }
}

// 18. Display Multiples of 10 (Table of 10)
public class MultiplesOfTen {
    public static void displayTableOfTen() {
        System.debug('Table of 10:');
        for (Integer i = 1; i <= 10; i++) {
            Integer result = 10 * i;
            System.debug('10 x ' + i + ' = ' + result);
        }
    }
}