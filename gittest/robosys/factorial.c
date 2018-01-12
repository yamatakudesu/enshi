#include<stdio.h>

int main(void) {
  int x, y;
  double z;

  scanf("%d %d %lf", &x, &y, &z);

  int fact, gcd, lcm;
  double sqrt;

  fact = fact(x);
  gcd = gcd(x, y);
  lcm = lcm(x, y);

  printf("")
  
  
  return 0;
}

int fact(int x) {
  int fact = 1; 
  for(int i=1; i<=x; i++){
    fact = fact * i;　//factに1からxまでの整数をかける
  }
  return fact; //xの階乗であるfactを返す
}

double sqrt(double x) {
  

}

int gcd(int x, int y) {
  if (x > y) {
    x = x - y;  //x>yならxにx-yを代入し,gcd関数を再び行う
    gcd(x, y);
  } else if (x < y) { 
    y = y - x;  //x<yならyにy-xを代入し,gcd関数を再び行う
    gcd(x, y);
  } else {
    return x;  //x=yなら値xを返す
  }
}

int lcm(int x, int y) {
  return x * y / gcd(x,y); //xとyの積を、xとyの最大公約数で割った値を返す
}

  
