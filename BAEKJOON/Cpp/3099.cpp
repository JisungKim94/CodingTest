#include <iostream>
#include <string>
using namespace std;

string tekst;
int brojKomandi[256];
int brojKomandi2[256];

void PostaviManji(int &stari, int novi)
{
	if (novi < stari) stari = novi;
}

int main(void)
{
	cin >> tekst;
	int n = tekst.length();
	for (int i = 0; i < n; i++)
		if (tekst[i] < 'A' || tekst[i] > 'Z')
			return 0;

	for (char mem = 'A'; mem <= 'Z'; mem++)
		brojKomandi[mem] = n * 2;
	brojKomandi[tekst[0]] = 2;

	for (int i = 1; i < n; i++)
	{
		for (char mem = 'A'; mem <= 'Z'; mem++)
			brojKomandi2[mem] = n * 2;

		for (char mem = 'A'; mem <= 'Z'; mem++)
			if (brojKomandi[mem] != n * 2)
				if (tekst[i] == mem)
					PostaviManji(brojKomandi2[mem], brojKomandi[mem] + 1);
				else
				{
					PostaviManji(brojKomandi2[mem], brojKomandi[mem] + 2);
					PostaviManji(brojKomandi2[tekst[i]], brojKomandi[mem] + 2);
				}

		for (char mem = 'A'; mem <= 'Z'; mem++)
			brojKomandi[mem] = brojKomandi2[mem];
	}

	int min = n * 2;
	for (char mem = 'A'; mem <= 'Z'; mem++)
		PostaviManji(min, brojKomandi[mem]);

	cout << min << endl;
    return 0;
}