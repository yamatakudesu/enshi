/* test0.c */
#include <stdio.h>

/*
引数：整数i,j
返り値：iとjの積
機能：引数の積を計算し返す関数
*/
int test(int i, int j){
  return (i * j);
}

int main(int arg, char *argv){
  int i,j,k;　//入力となる整数i,jとその積k
  i = 3;
  j = 2;
  k = test(i,j);  //i,jをかけてkに代入する

  /*kの値が5より大きければ">5"と表示し
    そうでなければ"<=5"を表示する*/
  if (k > 5) printf(">5\n");　　
  else printf("<=5\n");
  return 0;
}
