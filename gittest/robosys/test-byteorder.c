#include <stdio.h>
int print_byte (unsigned int s) {
  int i;
  unsigned char *p;
  p = (unsigned char*)&s;
  for (i = 0; i < sizeof(unsigned int); i++) {
    printf("%02x", *p);
    p++;
  }
  printf("\n");
}
int print_byte2 (unsigned short s) {
  int i;
  unsigned char *p;
  p = (unsigned char*)&s;
  for (i = 0; i < sizeof(unsigned short); i++) {
    printf("%02x", *p);
    p++;
  }
  printf("\n");
}
int print_byte3 (unsigned long s) {
  int i;
  unsigned char *p;
  p = (unsigned char*)&s;
  for (i = 0; i < sizeof(unsigned long); i++) {
    printf("%02x", *p);
    p++;
  }
  printf("\n");
}
int main (int argc, char* argv[]) {
  unsigned int u1;
  unsigned short u2;
  unsigned long u3;
  u1 = 0x1234abcd; u2 = 0x1234abcd; u3 = 0x1234abcd;
  printf("u1 = %x : ", u1); print_byte(u1);
  printf("u2 = %x : ", u2); print_byte2(u2);
  printf("u3 = %lx : ", u3); print_byte3(u3);
}
