// Implement Greedy search algorithm for any of the following application:
// I. Selection Sort

import java.util.*;
public class selection_sort{
    void selSort(int arr[])
    {
        for (int i=0;i<arr.length-1;i++)
        {
            int index=i;

            for(int j=i+1;j<arr.length;j++)
            {
                if(arr[j]<arr[index])
                {
                    index = j;
                }
            }

            int smallerno = arr[index];
            arr[index] = arr[i];
            arr[i] = smallerno;
            
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("\nHow many no.s in array? :");
        
        int n = sc.nextInt();

        int arr1[] = new int[n];
        System.out.println("\nEnter array elements: ");
        for(int i=0;i<n;i++)
        {
            arr1[i] = sc.nextInt();
        }

        selection_sort s = new selection_sort();
        s.selSort(arr1);
        System.out.println("The sorted array is: ");
        for(int i=0;i<n;i++)
        {
            System.out.print(arr1[i]+" ");
        }
         sc.close();
        
    }
}