#include "bola.h"

using namespace std;

int main()
{
    bola B;
    cout << "Masukkan jari-jari : "; cin >> B.jarijari;
    cout << endl;

    luasPermukaanBola(B);
    volumeBola(B);
    cout << "Diameter bola " << diameterBola(B.jarijari) << endl;

    return 0;
};
