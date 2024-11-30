package Letter;

public class Letter {
    private String sender;
    private String recipient;
    private String body;

    public Letter(String s, String r) {
        this.sender = s;
        this.recipient = r;
        this.body = " ";
    }

    public void addLine(String line) {
        this.body = this.body.concat(line).concat("\n");
    }

    public String getText() {
        String letter = "Caro, ".concat(this.sender);
        letter = letter.concat("\n");
        letter = letter.concat(this.body).concat("\n");
        letter = letter.concat("\n");
        letter = letter.concat("Tuo,\n");
        letter = letter.concat(this.recipient);
        return letter;

    }

}
