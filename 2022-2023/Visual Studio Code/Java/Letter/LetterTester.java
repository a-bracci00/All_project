package Letter;

public class LetterTester {
    public static void main(String[] args) {
        Letter l = new Letter("gabri", "giovanni");
        l.addLine("Ciao Giovanni");
        ;
        System.out.println(l.getText());

    }
}
