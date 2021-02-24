#include <iostream>
#include <cstring>

using namespace std;

int main(){
  int n;
  cin >> n;
  string s;
  cin >> s;
  int sum = 0;
  for(int i=0; i<n; i++){
    for(int j=i; j<n; j++){
      if(s[i] == s[j]){
        continue;
      }
      for(int k=j; k<n; k++){
        if((j-i!=k-j) && (s[i]!=s[k]) && (s[j]!=s[k])){
          sum++;
        }
      }
    }
  }
  cout << sum <<endl;
  return 0;
}
