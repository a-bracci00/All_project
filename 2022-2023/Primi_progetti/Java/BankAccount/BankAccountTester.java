package BankAccount;

public class BankAccountTester {
    public static void main(String[] args) {
        BankAccount ba = new BankAccount(1000, 100);
        System.out.println(ba.getBalance());
        System.out.println(ba.withdraw(500));
        System.out.println(ba.withdraw(400));
        System.out.println(ba.getBalance());
        ba.addIntersest(20);
        System.out.println(ba.getBalance());
    }
}
