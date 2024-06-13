
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        final char[] parentheses = bf.readLine().toCharArray();
        Stack<Character> stack = new Stack<>();
        int result = 0;

        for (int i = 0; i < parentheses.length; i++) {
            if (parentheses[i] == '(') {
                stack.push(parentheses[i]);
            } else if (parentheses[i] == ')') {
                stack.pop();
                if (parentheses[i - 1] == '(') {
                    result += stack.size();
                } else {
                    result += 1;
                }
            }
        }
        System.out.println(result);
    }
}