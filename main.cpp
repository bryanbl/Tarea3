#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

char* str1 = "Yooy sooy del ITM";
char* str2 = "oy";

bool search_Word(char *cadena1, char *cadena2);

int main()
{
    bool res;
    res=search_Word(str1,str2);

    cout<<res<<endl;
}

bool search_Word(char* cadena1, char* cadena2)
{
    str1 = cadena1;
    str2 = cadena2;
    int j = 0;
    int contador=0;

    for(int i = 0; i<(strlen(str1));i++)
    {
        if(str1[i]==str2[i])
        {
            contador +=1;
        }
        else
        {
            i -= contador;
            contador=0;
        }

        if (contador=strlen(str2))
        {
            return 1;

        }
    }
    return 0;
}
