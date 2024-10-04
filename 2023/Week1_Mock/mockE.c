#include <stdio.h>
#include <stdlib.h>

int main() {
    int testCases;
    
    scanf("%d", &testCases);
    
    int *nums = malloc(testCases * sizeof(int));
    
    for (int i = 0; i < testCases; i++) {
        scanf("%d", &nums[i]);
    }
    
    printf("%d\n", nums[0]);
    
    free(nums);
    
    return 0;
}
