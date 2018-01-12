/* test0a.c */
#include <stdio.h>

/*
引数：整数i,j
返り値：iとjの積
機能：引数の積を計算し返す関数
*/
int test(int i, int j){
  return (i * j);
}

int main(int argc, char *argv[]){

  int i = atoi(argv[1]); //コマンドライン引数の1つ目をint型にしてiに代入
  int j = atoi(argv[2]); //コマンドライン引数の2つ目をint型にしてjに代入

  int k = test(i, j);
  
  /*kの値が5より大きければ">5"と表示し
    そうでなければ"<=5"を表示する*/
  if (k > 5) {
    printf(">5\n");
  } else {
    printf("<=5\n");
  }
  return 0;
}
