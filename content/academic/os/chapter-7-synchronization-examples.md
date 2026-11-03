---
title: Chapter 7 - Synchronization Examples
tags:
- academic
- os
aliases:
- Chapter 7 - Synchronization Examples
---

## Readers-Writers
```cpp
#include<bits/stdc++.h>
using namespace std;

int mutx = 0;
void wait_mutx() {
    while (mutx) {
        // wait
    }
    mutx = 1;
}
void signal_mutx() {
    mutx = 0;
}

int rw_mutx = 0;
void wait_rw_mutx() {
    while (rw_mutx) {
        // wait
    }
    rw_mutx = 1;
}
void signal_rw_mutx() {
    rw_mutx = 0;
}

// action = 0 -> leave
// action = 1 -> enter

void writer(int action) {
    if (action) {
        wait_rw_mutx();
        cout << "Writer is writing..." << endl;
        sleep(1); // Simulate writing time
    } else {
        signal_rw_mutx();
        cout << "Writer has finished writing." << endl;
        sleep(1); // Simulate time after writing
    }
}

int readers_count = 0;
void reader(int action) {
    if (action) {
        wait_mutx();
        readers_count++;
        if (readers_count == 1) {
            wait_rw_mutx();
        }
        signal_mutx();
        cout << "Reader is reading..." << endl;
        sleep(1); // Simulate reading time
    } else {
        wait_mutx();
        readers_count--;
        if (readers_count == 0) {
            signal_rw_mutx();
        }
        signal_mutx();
        cout << "Reader has finished reading." << endl;
        sleep(1); // Simulate time after reading
    }
}

int main() {
    thread t1(writer, 1);
    thread t2(reader, 1);
    thread t3(reader, 1);
    thread t4(reader, 0);
    thread t5(writer, 0);

    t1.join();
    t2.join();
    t3.join();
    t4.join();
    t5.join();

    return 0;
}
```

## Monitor

### Simple implementation
```cpp
#include<bits/stdc++.h>
using namespace std;

enum state { THINKING, HUNGRY, EATING };

class Philosopher {
    public:
        state s[5];
        Philosopher() {
            for(int i = 0; i < 5; i++) {
                s[i] = THINKING;
            }
        }
        void test(int i);
        void pickUp(int i);
        void putDown(int i);
};

void Philosopher::test(int i) {
    if (s[i] == HUNGRY && s[(i + 4)%5] != EATING && s[(i + 1) % 5] != EATING) {
        s[i] = EATING;
    }
    cout << "Philosopher " << i << " is " << (s[i] == EATING ? "EATING" : (s[i] == HUNGRY ? "HUNGRY" : "THINKING")) << endl;
}

void Philosopher::pickUp(int i) {
    s[i] = HUNGRY;
    if (s[i] != EATING) {
        test(i);
    }
    cout << "Philosopher " << i << " is " << (s[i] == EATING ? "EATING" : (s[i] == HUNGRY ? "HUNGRY" : "THINKING")) << endl;
    cout << "------------------------------------------" << endl;
}

void Philosopher::putDown(int i) {
    s[i] = THINKING;
    test((i + 4) % 5);
    test((i + 1) % 5);
}

int main() {
    Philosopher p;
    p.pickUp(0);
    p.pickUp(1);
    p.putDown(0);
    p.pickUp(2);
    return 0;
}
```

### With spinlock
```cpp
#include<bits/stdc++.h>
using namespace std;

enum state { THINKING, HUNGRY, EATING };

class Philosopher {
    public:
        state s[5];
        Philosopher() {
            for(int i = 0; i < 5; i++) {
                s[i] = THINKING;
            }
        }
        void test(int i);
        void pickUp(int i);
        void putDown(int i);
};

void Philosopher::test(int i) {
    if (s[i] == HUNGRY && s[(i + 4)%5] != EATING && s[(i + 1) % 5] != EATING) {
        s[i] = EATING;
    }
}

void Philosopher::pickUp(int i) {
    s[i] = HUNGRY;
    while (s[i] != EATING) {
        test(i);
    }
    printf("Philosopher %d is %s\n", i, (s[i] == EATING) ? "EATING" : "HUNGRY");
}

void Philosopher::putDown(int i) {
    s[i] = THINKING;
}

int main() {
    Philosopher p;
    thread t[5];
    t[0] = thread(&Philosopher::pickUp, &p, 0);
    t[1] = thread(&Philosopher::pickUp, &p, 1);
    t[2] = thread(&Philosopher::putDown, &p, 0);
    t[3] = thread(&Philosopher::putDown, &p, 1);

    t[0].join();
    t[1].join();
    t[2].join();
    t[3].join();

    return 0;
}
```

### Without spinlock
```cpp
#include<bits/stdc++.h>
using namespace std;

enum state { THINKING, HUNGRY, EATING };

class Philosopher {
    public:
        state s[5];
        Philosopher() {
            for(int i = 0; i < 5; i++) {
                s[i] = THINKING;
            }
        }
        void test(int i);
        void pickUp(int i);
        void putDown(int i);
};

void Philosopher::test(int i) {
    if (s[i] == HUNGRY && s[(i + 4)%5] != EATING && s[(i + 1) % 5] != EATING) {
        s[i] = EATING;
        printf("Philosopher %d is %s\n", i, (s[i] == EATING) ? "EATING" : "HUNGRY");
        pickUp(i);
    }
}

void Philosopher::pickUp(int i) {
    if (s[i] != EATING) {
        s[i] = HUNGRY;
        test(i);
    }
}

void Philosopher::putDown(int i) {
    s[i] = THINKING;
    test((i + 4) % 5);
    test((i + 1) % 5);
}

int main() {
    Philosopher p;
    thread t[5];
    t[0] = thread(&Philosopher::pickUp, &p, 0);
    t[1] = thread(&Philosopher::pickUp, &p, 1);
    t[2] = thread(&Philosopher::putDown, &p, 0);
    t[3] = thread(&Philosopher::putDown, &p, 1);

    t[0].join();
    t[1].join();
    t[2].join();
    t[3].join();

    return 0;
}
```
