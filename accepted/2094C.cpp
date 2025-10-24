#include <iostream>
#include <unordered_set>

using namespace std;
int main() {
	unsigned T;
	cin >> T;
	for(unsigned t = 0; t < T; ++t) {
    	unsigned N;
    	cin >> N;
    
    	unsigned G[N][N];
    	for(unsigned n1 = 0; n1 < N; ++n1) {
    		for (unsigned n2 = 0; n2 < N; ++n2) cin >> G[n1][n2];
    	}
    
    	unordered_set<unsigned> S;
    	for(unsigned i = 1; i <= N*2; ++i) S.insert(i);
    	
    	unsigned permutation[N*2], i = 0, j = 0;
    	while(i < N) {
    		permutation[i+j + 1] = G[i][j];
    		
    		S.erase(G[i][j]);
    		
    		if(i <= j) i += 1;
    		else j += 1;
    	}
    	
    	permutation[0] = *S.begin();
     
        for (unsigned i = 0; i < N*2; ++i) {
            if (i < (N*2) - 1) cout << permutation[i] << ' ';
            else cout << permutation[i] << '\n';
        }
    }
    
	return 0;
}