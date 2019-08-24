#include <iostream>

// C++ program to demonstrate array of strings using 
// 2D character array 
#include<stdio.h> 

using namespace std; 

int main() 
{ 
	// Initialize 2D array 
	char colour[4][10] = {"Blue", "Red", "Orange", 
					"Yellow"}; 
	
	// Printing Strings stored in 2D array 
	for (int i = 0; i < 4; i++) 
		cout << colour[i] << "\n"; 
		
	// Initialize String Array 
    string color[4] = {"Blue", "Red", "Orange", "Yellow"}; 
      
    // Print Strings 
    for (int i = 0; i < 4; i++)  
        cout << color[i] << "\n";
        
    // declare and initialize string 
    char str[] = "Geeks"; 
      
    // print string
    printf("%s\n",str);
    
    // declaring string 
    char str1[50]; 
      
    // reading string 
    scanf("%s",str1); 
      
    // print string 
    printf("%s",str1); 
	
	return 0; 
} 
