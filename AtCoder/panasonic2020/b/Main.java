import java.util.*;

// WA
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int w = sc.nextInt();
        System.out.println((long) (Math.ceil((double) h * (double) w / 2)));
    }
}
