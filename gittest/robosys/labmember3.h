class LabMember {
 protected:
  char name[32];

 public:
  LabMember(char* _name) {
    strcpy(name, _name);
  }
  ~LabMember() {
  }

  char* GetName() {
    return name;
  }
};
