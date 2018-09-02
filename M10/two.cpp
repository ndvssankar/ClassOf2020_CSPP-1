#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef vector<ll> hn;
const ll M = 10e13;

void tri_pent(ll n, int a, int b) {
	ll s = 1;
	ll t = 1;
	std::vector<ll> tn;
	std::vector<ll> pn;
	tn.push_back(s);
	pn.push_back(t);
	int k = 2;
	int i = 1;
	int j = 4;
	while(pn.back() <= n) {
		tn.push_back(tn.back() + k);
		pn.push_back(pn.back() + j);
		// tn[i] = tn[i-1] + k;
		// pn[i] = pn[i-1] + j;
		k=k+1;
		j=j+3;
		i=i+1;
	}
	for(std::vector<ll>::iterator it = pn.begin() ; it != pn.end(); ++it) {
		// cout<< ' '<< *it;
    	if (std::binary_search (tn.begin(), tn.end(), *it))
    		cout<<*it<<endl;
	}
}

void pent_hex(ll n, int a, int b) {
	std::vector<ll> pn;
	std::vector<ll> hn;
	pn.push_back(1);
	pn.push_back(5);
	hn.push_back(1);
	hn.push_back(6);
	int i = 2;
	int j = 7;
	int k = 9;
	while(hn.back() <= n) {
		pn.push_back(j + pn.back());
		hn.push_back(k + hn.back());
		j = j + 3;
		k = k + 4;
		i = i + 1;
	}
	for(std::vector<ll>::iterator it = hn.begin() ; it != hn.end(); ++it) {
		// cout<< ' '<< *it;
    	if (std::binary_search (pn.begin(), pn.end(), *it))
    		cout<< *it<<"\n";
	}
}

int main() {
	ll n;
	int a, b;
	cin>>n;
	cin>>a;
	cin>>b;
	if(a<b && a == 3 && b == 5)
		tri_pent(n, a, b);
	else if(a<b && a == 5 && b == 6)
		pent_hex(n, a, b);
	return 1;
}
