import java.util.*;

class Main {
    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Main().run();
    }

    private void run() {
        int n = sc.nextInt();
        int[] b = new int[n-1];

        for (int i = 0; i < n - 1; i++) {
            b[i] = sc.nextInt();
        }

        int ans = b[0];
        for (int i = 1; i < n - 1; i++) {
            ans += Math.min(b[i], b[i - 1]);
        }
        ans += b[n - 2];
        System.out.println(ans);
    }
}

