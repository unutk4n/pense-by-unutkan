# INTERFACES AND CABLES

<picture> 
<img alt = "ccna1" src = "md_files/pictures/ccna1.png">
</picture>
The most fundamental and essential thing while connecting things is RJ-45 Cable. (a.k.a. Ethernet cable, cat 5, cat6, cat7)
## Ethernet: 
Ethernet is a collection of network protocols/standards.

## Why do we need network standards/protocols?
To make it possible to communicate. Without phsical and logical protocols it would be something like two people trying to speak in different languages.  

## Bits and Bytes
Connections between devices in a network operates at a set speed. These speeds are measured in bits per second.
A bit is either a 0 or a 1.
A byte is equal to 8 bits.
Speed is measured in bits per second like Kbps, Mbps, Gbps, etc. Not bytes per second. It's also worth to note that Data on a hard drive for example is measured in bytes not bits!
<b> This means Gigabyte is 8 times larger than a gigabit<b>

<picture> 
<img alt = "ccna2" src = "md_files/pictures/ccna2.png">
</picture>

## Ethernet Standards

These standards are set by Institute of Electrical and Electronics Engineers a.k.a. IEEE. IEEE 802.3 standard in 1983 

You’ll notice that all ethernet standards start with IEEE 802.3 

<picture> 
<img alt = "ccna3" src = "md_files/pictures/ccna3.png">
</picture>


You can see the standards with their own speed, common name, informal name and the length that the cable can go.

Informal name: numbers are obviously the speed numbers base refers to baseband signaling (not on this leeson) T means twisted pair (also not in this lesson) 

Copper wires that’s used for these speeds are UTP cables – Unshielded  Twisted Pair  

Unshielded means that there is no metalic protection and is vulnerable to damages. It’s twisted because this protects against EMI –Electromagnetic Interference 

There are 4 pairs (8 in total) of copper wires in UTP Cables. Not every standard use every single copper wire. For example 10Base-T and 100Base-T standards use only 2 pairs(4 wires) 

1000Base-T and 10GBase-T use 4 pairs(8wires) 

## Let's connect things!
### Computer - Switch
<picture> 
<img alt = "ccna4" src = "md_files/pictures/ccna4.png">
</picture>

Computers use wire 1 and 2 to Transmit data (Tx) and wire 3 and 6 to Receive data (Rx) 

Switches use wire 1 and 2 to Receive data (Rx) and wire 3 and 6 to Transmit data (Tx) 

This type of transmission is called Full-Dublex Transmission. It allows devices to transmit and receive bits at the same time. No collisions will happen . 

### Router - Switch

<picture> 
<img alt = "ccna5" src = "md_files/pictures/ccna5.png">
</picture>

The wires that’s being used for by the router is the same with pc.  

Connections made with the cables are called Straight-through cable because 1 is connected to 1, 2 is connected to 2, 3 is connected to 3 and so on.

### Switch - Switch

<picture> 
<img alt = "ccna6" src = "md_files/pictures/ccna6.png">
</picture>

In this case we can’t use straight-through cable because it won’t work. The pin protocols doesn’t suit.  

In that case we have a cable type called Crossover. This cable allows us to connect same devices to each other or devices that has the same pins with same protocols. 


<picture> 
<img alt = "ccna7" src = "md_files/pictures/ccna7.png">
</picture>


## Auto MDI - X

It’s worth to note that modern internet devices make it easy to work with because they have cool features. One feature is “Auto MDI-X" this feature allows the device to change the transmit and receive pins so that it can connect easily with a straight-through cable to any device. 



## 1000Base-T & 10GBase-T
On those two protocols all 4 pairs of cables are used(8pairs) 

The best part about these two protocols is that each pair is bidirectional. 
<picture> 
<img alt = "ccna8" src = "md_files/pictures/ccna8.png">
</picture>


## FIBER-OPTIC CONNECTIONS

<picture> 
<img alt = "ccna9" src = "md_files/pictures/ccna9.png">
</picture>

Usually to terminate the Fiber connection you have to use SFP's

<picture> 
<img alt = "ccna10" src = "md_files/pictures/ccna10.png">
</picture>

One cable is to receive and one to transmit
### Multimode
<picture> 
<img alt = "ccna11" src = "md_files/pictures/ccn11.png">
</picture>

Here you can see the layers of the fiberoptic cable

### Singlemode
<picture> 
<img alt = "ccna12" src = "md_files/pictures/ccna12.png">
</picture>


### Fiber-Optic Standards
<picture> 
<img alt = "ccna13" src = "md_files/pictures/ccna13.png">
</picture>

## Diffrences between UTP & Fiber-Optic
<picture> 
<img alt = "ccna14" src = "md_files/pictures/ccna14.png">
</picture>

