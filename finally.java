class FinallyExample {
    public static String test() {
        try {
            return "TRY";
        } finally {
            return "FINALLY";
        }
    }

    public static void main(String[] args) {
        System.out.println(test());
    }
}