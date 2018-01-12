#include <stdio.h>

int factorial(int);

/* program entry */
int main(int argc, char **argv) {
  int m, n;
  if (argc != 2) {
    printf("usage: %s n\n", argv[0]);
    return 1;
  }
  m = atoi(argv[1]);
  n = factorial(m);
  printf("factorial(%d) = %d\n", m, n);
  
  return 0;
}

/* factorial */
int factorial(int n) {
  if (n < 1) {
    return 0;
  }
  else if (n == 1) {
    return 1;
  }
  else {
    int m = factorial(n - 1);
    return m * n;
  }
}
