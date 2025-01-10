#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int k = 5;
    int numPrime = 300000;
    vector<int> primes = {2, 3};

    while (k < numPrime) {
        bool isPrime = true;
        int j = 0;
        while (j < primes.size() && isPrime && primes[j] <= sqrt(k)) {
            if (k % primes[j] == 0) {
                isPrime = false;
            }
            j++;
        }
        if (isPrime) {
            primes.push_back(k);
        }
        k += 2;
    }

    auto prime = [&](int numK) {
        return find(primes.begin(), primes.end(), numK) != primes.end();
    };

    auto percPrime = [&](const vector<int>& diagonalsK) {
        int j = 0;
        int numPrime = 0;
        while (j < diagonalsK.size()) {
            if (prime(diagonalsK[j])) {
                numPrime++;
            }
            j++;
        }
        return round(static_cast<double>(numPrime) / diagonalsK.size() * 100);
    };

    auto addLayer = [&](vector<int>& diagonalJ) {
        int j = 0;
        int x = static_cast<int>(sqrt(diagonalJ.back()) + 1);
        while (j < 4) {
            diagonalJ.push_back(diagonalJ.back() + x);
            j++;
        }
        return diagonalJ;
    };

    vector<int> diagonal = {1};
    int num = 1;
    bool solved = false;
    while (!solved) {
        num += 2;
        diagonal = addLayer(diagonal);
        int m = percPrime(diagonal);
        cout << m << endl;
        if (m < 10) {
            cout << num << endl;
            solved = true;
        }
    }

    return 0;
}
