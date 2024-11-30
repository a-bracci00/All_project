public class StringReplaceDemo {
    public static void main(String[] args) {
        String input = "Mississippi";
        String modified_input = input.replace("i", "ii");
        modified_input = modified_input.replace("ss", "s");
        System.out.println(modified_input);
    }
}