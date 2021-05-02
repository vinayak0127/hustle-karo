#include<bits/stdc++.h>

using namespace std;


string LongestCommonString(string str[], int n){
    if(n==0)return 0;
    if(n==1)return str[0];
    sort(str,str+n);
    string f= str[0],l = str[n-1];
    int i=0;
    int en = min(f.size(),l.size());
    while(i<=en && l[i] == f[i]){
        i++;
    }
    string pm = str->substr(0,i);
    return pm;
}


int main(){

    string s[] = {"flower","flow","flight"};
    int n = sizeof(s) / sizeof(s[0]);

    cout<<LongestCommonString(s,n)<<endl;
    return 0;
}
