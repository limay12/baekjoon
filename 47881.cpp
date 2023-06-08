#include <iostream>
using namespace std;
int arr[100000];
int N, K, ans;

int main() {
	cin >> N >> K;
	for(int i = 1; i <= N; i++){
		cin >> arr[i];
	}
	int index = 0;
	while(true){
		if(index >= N) break;
		if(index == 0) index += K;
		else index += K - 1;
		ans++;
	}
	cout << ans << endl;
	return 0;
}
