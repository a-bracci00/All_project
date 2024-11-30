public class StringReplaceDemo2 {
    public static void main(String[] args) {
        String sentence = "all work and no play makes jack a dull";
        sentence = sentence.trim();
        sentence = sentence.replace(" ", "");
        System.out.println(sentence);
    }
}