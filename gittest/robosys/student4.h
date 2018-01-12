class Student : public LabMember {
 private:
  int grade;

 public:
 Student() : LabMember() {}
 Student(char* _name) : LabMember(_name) {
    grade = 0;
  }
  ~Student() {
  }

  void SetGrade(int _grade) {
    grade = _grade;
  }
  int GetGrade() {
    return grade;
  }
  void PrintInfo() {
    printf("student name = %s, grade = %d\n", GetName(), GetGrade());
  }
  void promotion() {
    printf("student %s is going to be in the %dth(st, nd, rd) grade.", GetName(), GetGrade()+1);
  }
  
};
