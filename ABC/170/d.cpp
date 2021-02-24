#include <iostream>

using namespace std;

int main(){
  int n;
  cin >> n;
  if(n == 1){
    cout << 1 << endl;
    return 0;
  }
  int a[n];
  for(int i=0; i<n; i++){
    cin >> a[i];
  }
  sort(a, a+n);
  if(a[0] == 1){
    if(a[1] == 1){
      cout << 0 << endl;
      return 0;
    }else{
      cout << 1 << endl;
      return 0;
    }
  }

  bool check = true;
  int ans = 0;
  int dub[n];
  memset(dub, 0, n);
  int index = 0;
  for(int i=0; i<n; i++){
    if(i != 0){
      if(a[i-1] == a[i]){
        dub[index] = a[i];
        index++;
      }
    }
    for(int j=0; j<i; j++){
      if(a[j] != 1){
        if(a[j]*2 > a[i]){
          break;
        }
      }
      if(i == j){
        continue;
      }
      if(a[i]%a[j] == 0){
        check = false;
        break;
      }
    }
    if(check){
      ans += 1;
    }
    check = true;
  }

  int num = unique(dub, dub+index) - dub;
  for(int i=0; i<num; i++){
    ans -= count(a, a+n, dub[i]);
    // cout << dub[i] << endl;
  }


  // for(int i=0; i<n; i++){
  //   cout << a[i] << endl;
  // }
  cout << ans << endl;
}
