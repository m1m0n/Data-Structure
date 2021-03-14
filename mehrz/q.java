public class CircularPriorityQueue {
    int size;
    int front;
    int rear;
    int[] queArray;
    int nItems;
    public CircularPriorityQueue(int s) {
        size = s;
        queArray = new int[size];
        front = 0;
        rear = -1;
        nItems = 0;
    }
    public boolean isEmpty() {
        return nItems == 0;
    }
    public boolean isFull() {
        return nItems == size;
    }

    public void insert(int n) {
        if (isFull()) {
            System.out.println("Can't insert " + n + ", queue is full.");
        }
        else {
                int i, mod;
                for(i = rear;; i--) {
                    mod = negativeMod(i, size);
                    //System.out.println(i + ", " + mod);
                    if(n < queArray[mod])
                        queArray[negativeMod(mod + 1, size)] = queArray[mod];
                    else
                        break;
                }
                queArray[negativeMod(mod + 1, size)] = n;
                nItems++;
                if (rear == size-1)
                    rear = 0;
                else
                    rear++;
            
        }
    }
    public int remove() {
        if(isEmpty()) {
            System.out.println("Can't remove, queue is empty.");
            return -1;
        }
        else {
            int temp = queArray[front];
            // for testing, replace removed element with 0
            queArray[front] = 0;
            if(front == size-1)
                front = 0;
            else
                front++;
            nItems--;
            return temp;
        }
    }
    public int peek() {
        if(isEmpty()) {
            System.out.println("Can't peek, queue is empty.");
            return -1;
        }
        return queArray[front];
    }
    // only for testing
    public void display() {
        for(int i= queArray.length-1; i >= 0; i--)
            System.out.println(queArray[i]);
        System.out.println();
    }
    public static int negativeMod(int n, int m) {
        int a = n % m;
        if (a < 0)
            a += m;
        return a;
    }
    public static void main(String[] args) {
        CircularPriorityQueue q = new CircularPriorityQueue(5);
        q.insert(10);
        q.display();

        q.insert(20);
        q.display();
        q.remove();

        q.display();
        q.remove();
        q.display();

        q.insert(10);
        q.display();

        q.insert(20);
        q.display();

        q.insert(30);
        q.display();

        q.insert(40);
        q.display();

        q.insert(50);
        q.display();
    
        q.remove();
        q.display();
        q.insert(60);
        q.display();
    }
}