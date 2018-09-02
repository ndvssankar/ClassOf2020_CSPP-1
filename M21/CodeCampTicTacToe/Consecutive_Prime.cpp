#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
const unsigned long long MAX  = 100000000;

void gen_primes(vector <int> &primes) {
    bool marked[MAX/2 + 1] = {0};
    for (int i=1; i<=(sqrt(MAX)-1)/2; i++)
        for (int j=(i*(i+1))<<1; j<=MAX/2; j=j+2*i+1)
            marked[j] = true;

    primes.push_back(2);

    for (int i=1; i<=MAX/2; i++)
        if (marked[i] == false)
            primes.push_back(2*i + 1);
}

int find_length(int limit, vector<int> &prime, long long int sum_prime[]) {
    int max_length = -1;
    int prime_number = -1;
    for (int i=0; prime[i]<=limit; i++) {
        for (int j=0; j<i; j++) {
            if (sum_prime[i] - sum_prime[j] > limit)
                break;
            long long int consSum  = sum_prime[i] - sum_prime[j];
            if (binary_search(prime.begin(), prime.end(), consSum)) {
                if (max_length < i-j+1) {
                    max_length = i-j+1;
                    prime_number = consSum;
                }
            }
        }
    }
    cout<<prime_number<<" "<<max_length<<endl;
    return prime_number;
}


int main() {
    int t;
    cin>>t;
    vector<int> primes;
    gen_primes(primes);
    long long int sp[primes.size() + 1];
    sp[0] = 0;
    for (int i = 1 ; i <= primes.size(); i++)
        sp[i] = primes[i-1] + sp[i-1];  
    
    for(int i=0; i<t; i++) {
        long input_value;
        cin>>input_value;
        find_length(input_value, primes, sp);
    }
}