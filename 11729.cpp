using namespace std;

void func(int a, int b, int n){
    if(n == 1){
        cout << a << ' ' << b << '\n';
        return;
    }
    func(a, 6-a-b, n-1);
    cout << a << ' ' << b <<'\n';
    func(6-a-b, b, n-1);
}
int main(void){
    # 입출력 속도를 가속시키기 위한 용도
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    cout << (1<<n) - 1 << '\n';
    func(1, 3, n);
}
