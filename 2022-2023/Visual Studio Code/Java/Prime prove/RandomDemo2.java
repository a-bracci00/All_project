import java.util.Random;

public class RandomDemo2 {
    public static void main(String[] args) {
        Random r = new Random();
        int a = r.nextInt(6);
        System.out.println(a);
    }
}
