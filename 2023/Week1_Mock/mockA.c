#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char string[100];
    fgets(string, sizeof(string), stdin);
    string[strcspn(string, "\n")] = 0;

    char *eye = strstr(string, "()");
    if (eye == NULL) {
        printf("fix\n");
        return 1; 
    }

    int left = abs(eye - string); 
    int right = abs(strlen(string) - (left + 2)); 

    if (left == right) {
        printf("correct");
    } else {
        printf("fix");
    }
    return 0;
}
