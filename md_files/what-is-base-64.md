# What is Base64?
Base64 is an encoding algorithm that allows you to transform any characters into an alphabet which consists of Latin letters, digits, plus, and slash. Thanks to it, you can convert Chinese characters, emoji, and even images into a “readable” string, which can be saved or transferred anywhere.

To figuratively understand why base64 was invented, imagine alice wants to share a picture with bob, the first issue here is that alice can't just describe it. She needs to convert the image into binary and tell bob that picture is converted into it. The second issue is that the phone bills. It's too expensive because each byte is represented as 8 binary digits. So they agree to use a more efficient way which is replacing every sic digit into one letter.

So "010001" this becomes "R" this.


# History

The history of the Base64 started long ago, in those times when engineers argued how many bits should be in a byte. Now we use eight-bit bytes, but before that were used seven-bit, six-bit, and even three-bit bytes. By the time the eight-bit encoding was approved as a standard, many systems used old encodings and did not support the “new standard”. This led to the fact that some data was simply lost during the transfer between the new and the old systems. For example, a mail server may discard the eighth bit when sending emails. Moreover, there was another problem with mail servers — they could only send text, but not binary data (such as images, video, archives). And so, in a magical way, clever minds develop an algorithm to solve these problems. Of course, over time, other binary-to-text encodings were developed, but thanks to the simplicity, efficiency and portability, Base64 became the most popular and was used almost everywhere.

For the first time the algorithm was described back in 1987 by a document describing the PEM protocol (if you are interested in the details, check the RFC 989 § 4.3). Since then, the algorithm has evolved, giving rise to new standards that are actively used throughout the world of IT.

# Size
During encoding, the Base64 algorithm replaces each three bytes with four bytes and, if necessary, adds padding characters, so the result will always be a multiple of four. Simply put, the size of the result will always be 33% (more exactly, 4⁄3) larger than the original data. The formula for calculating the length of the result string without padding is as follows: n * 4 / 3, where n is the length of the original data. 


# Algorithm

## Encoding 
The Base64 encode algorithm converts any data into plain text. Technically, it can be said that  it converts eight-bit bytes into six-bit bytes.  
For example, you have the “ABC” string and want to convert it to Base64: 
 
    First, you need to split the string letter by letter. Thus, you got 3 groups: 
        A 
        B 
        C 


 Next you need to convert each group to binary. To do this, for each letter you need to find the corresponding binary value in the ASCII table. Thus, now you have 3 groups of ones and zeros: 

    01000001 
    01000010 
    01000011 


	Now concatenate all the binary values together (that is, glue all the groups along and make sure you get a total of 24 characters): 
010000010100001001000011 

 Then, divide the resulting string into groups so that each one has 6 characters (if the last group has less than 6 characters, you need to fill it with zeros until it reaches the desired length). Well and good, now you have 4 groups: 

    010000 
    010100 
    001001 
    000011 

 At this step you have to convert six-bit bytes into eight-bit bytes. To do this, prepend the prefix “00” (two zeros) in front of each group: 

    00010000 
    00010100 
    00001001 
    00000011 


There you have to convert each group from binary to decimal by finding its corresponding decimal value in the ASCII table. If you did everything right, each group will be transformed into its integer number as follows: 

    16 
    20 
    9 
    3 


 Integer numbers obtained in the previous step are called “Base64 indices”. They are easy to remember, because it is a zero-based numbering, where each index corresponds to a Latin letter. It starts with the letter “A” in alphabetical order (i.e., A=0, B=1, C=2, D=3, and so on). For complete list, see Base64 Characters Table. So, matching indexes, convert them to corresponding letters: 

    Q 
    U 
    J 
    D 


The final chord, concatenate all letters to get the Base64 string: 
QUJD  

## Decoding 



    First, you need to split the string letter by letter. Thus, you got 4 groups: 
        Q 
        U 
        J 
        D 

    Each group (letter) is a Base64 character that has its own index, and now your task is to convert groups to indices. To do this, by mapping values from the Base64 Characters Table replace each character by its index (if you cannot find an index for a specific group, just discard it). All in all, you should get the following indices: 
        16 
        20 
        9 
        3 

    At this step you should convert each group from decimal to binary. So find corresponding decimal values in the ASCII table and make sure you get the following binary values: 
        00010000 
        00010100 
        00001001 
        00000011 

    Now remove the prefix “00” (two zeros) in front of each group: 
        010000 
        010100 
        001001 
        000011 

    There you have a simple concatenation of previous groups (that is, glue all the binary values together and get an 24-character string): 
    010000010100001001000011 

    Then, divide the resulting string into groups so that each one has 8 characters (if the last group has less than 8 characters, you must discard it). Now you have 3 groups of eight-bit bytes: 
        01000001 
        01000010 
        01000011 

    Once again using the ASCII table, convert all binary values into their ASCII characters: 
        A 
        B 
        C 
 
    The final chord, concatenate all ASCII characters to get the result string: 
    ABC 



The "b" in the base64 library refers to bytes.

In Python, strings are usually represented as Unicode (text data). However, Base64 encoding works with binary data (bytes), not text. This is why when you encode a string using Base64, you first need to convert it into a byte representation. When you call .encode("utf-8"), you're converting the string into a bytes object, which is what Base64 needs to perform the encoding.

For example:

    text.encode("utf-8") converts a string into bytes (b"text").
    base64.b64encode(b"text") performs Base64 encoding on the byte representation of the text.

So, "b" denotes that the data being passed or received is in bytes format.
