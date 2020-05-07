# Python Tetris

The backend logic of the game like collisions, movement, and clearing are based on arrays. 

## Tetrominoe Representation
Each tetrominoe is represented in a square array of 4 rows by 4 columns, where the empty spaces are 0's and the tetrominoes are 1's. 
Except each array is reresented as a number in binary to be more efficient. Each row starting at row 0 consist of 4 bits of a number starting from the most significant 16th bit. 

Here are all of the tetrimoes:

Z = 864 = 0b0000001101100000  
0	0	0	0  
0	0	1	1   
0	1	1	0   
0	0	0	0   

S = 1584 = 0b0000011000110000  
0	0	0	0   
0	1	1	0   
0	0	1	1  
0	0	0	0   

T = 624 = 0b0000001001110000  
0	0	0	0  
0	0	1	0  
0	1	1	1  
0	0	0	0   

Sq = 1632 = 0b0000011001100000  
0	0	0	0  
0	1	1	0  
0	1	1	0   
0	0	0	0   

L = 17504  = 0b0100010001100000  
0	1	0	0   
0	1	0	0   
0	1	1	0  
0	0	0	0   

Inverted L = 17600 = 0b0100010011000000  
0	1	0	0  
0	1	0	0   
1	1	0	0  
0	0	0	0  

I = 17476 = 0b0100010001000100  
0	1	0	0  
0	1	0	0  
0	1	0	0  
0	1	0	0  
 
The tetrominoes can be rotated by rotating the array via bitwise operation. 