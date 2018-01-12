#include<stdio.h>

#define FALSE 0 //FALSEを0に変換
#define TRUE 1 //TRUEを1に変換

int Debug = FALSE; //DebugにFALSEを代入

int fact (int x) {
  /*
    xが0以上の時、
    DebugがFALSEなら
    xの値をprintし
    xとfact(x-1)の積を返す
    DebugがFALSEでないなら
    xの値とreturn 1をプリントし
    1を返す
  */
  
  if (x >= 0) {
    if (Debug){
      printf("x = %d\n", x);
    }
    return (x * fact(x-1));
  } else {
    if (Debug) {
      printf("x = %d, return 1\n", x);
    }
    return 1;
  }
}

int main (int argc, char *argv[]) {
  int x, ret;

  /*
    パラメータが1以上あり、かつ1番目のパラメータ文字列の0文字目が'-'の時以下のループ
    ・1番目のパラメータ文字列の2文字目が'd'の時DebugにTRUEを代入し、switchから脱出
    ・argcの値を-1し、argvの値を+1する
  */
  while ((argc > 1) && (argv[1][0] == '-')) {
    switch (argv[1][1]){
    case 'd':
      Debug = TRUE;
      break;
    }
    argc--; argv++;
  }
  
  x = atoi(argv[1]);  //1番目のパラメータ文字列をint型数値に変換しxに代入
  ret = fact(x);  //retにfact(x)を代入
  printf("ret = %d\n", ret);  //retの値をprint
}

  
