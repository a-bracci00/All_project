package BankAccount;

public class BankAccount {

    private double balance;

    // private double interest;

    public BankAccount() {
        this.balance = 0;
        // this.interest = 0 / 100.0;
    }

    public BankAccount(double b, double i) {
        this.balance = b;
        // this.interest = i;
    }

    public double getBalance() {
        return this.balance;
    }

    public void deposit(double balanceToAdd) {
        this.balance += balanceToAdd;
    }

    public boolean withdraw(double moneyToRemove) {
        if (moneyToRemove > this.balance) {
            System.out.println("l'ammontare richiesto è maggiore del saldo");
            return false;
        } else {
            this.balance -= moneyToRemove;
            return true;
        }
    }

    public boolean addIntersest(double percentage) {
        if (percentage < 0 || percentage > 100) {
            return false;
        } else {
            percentage = percentage / 100.0;
            this.balance = this.balance + (this.balance * percentage);
            return true;
        }
    }

}