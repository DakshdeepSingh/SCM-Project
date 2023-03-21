#include<stdio.h>
void main()
{
    int arr1[2][3]={{1,2,3},{4,5,6}},arr2[3][2]={{7,8},{9,10},{11,12}},arr3[2][2],a=sizeof(arr1)/sizeof(arr1[0]),b=sizeof(arr2[0])/sizeof(arr2[0][0]);
    for (int i=0;i<a;i++)
    {
        for (int j=0;j<b;j++)
        {
            int temp=0;
            for (int k=0; k<=b;k++)
                temp+=(arr1[i][k]*arr2[k][j]);
            arr3[i][j]=temp;
        }
    }
    for (int i=0;i<a;i++)
    {
        for (int j=0;j<b;j++)
            printf("%d ",arr3[i][j]);
        printf("\n");
    }
}
