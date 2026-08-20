# Hackpad-Something-Something

This is a hardware project i.e. creating a macropad from scratch. 
My macropad in particular features a 12 key arrangement in a 4 column 3 row format. 
I used the SW_CHERRY_MX 1u as my mechanical keyboard switch and the 1N4148 diode connected to Module Seeduino xiao which acts as my microcontroller.

The Schematic of the project is given below.
<img width="1097" height="699" alt="Schematic" src="https://github.com/user-attachments/assets/49e94119-45c7-44c6-885a-413ef037d48c" />

Based on the Schematic I created the PCB design. 
<img width="638" height="595" alt="Screenshot_20260820_212827" src="https://github.com/user-attachments/assets/31844db4-8e37-464f-90df-70659172ee54" />
<img width="1087" height="655" alt="Screenshot_20260819_230059" src="https://github.com/user-attachments/assets/d51166b3-01da-4e8d-93a4-a25f5e4f1637" />
<img width="1027" height="611" alt="Screenshot_20260819_230111" src="https://github.com/user-attachments/assets/ed1db406-7e72-4dc6-b672-1486edd65bf7" />


The total dimension of the PCB came out to be 99.552*91.0 mm 
Using the PCB as base I created the case to enclose the hackpad.

# Firmware
For the firmware I used KMK instead of the other popular ones. This decision was mostly because of my comfort in python and ease and simple to write code of KMK.

# Final design of the macropad

I used FreeCAD for the design of the macropad's case and it was not fun. I searched tutorials and it only existed for other stuff so I looked at the other stuff's tutorial and applied it to the macropad.
The final design is well not the best to be frank but I made it myself so I am quite proud of it. 
<img width="1206" height="737" alt="Screenshot_20260820_234229" src="https://github.com/user-attachments/assets/d1005b8c-28d7-42ef-8cbd-75d9487ef763" />
<img width="930" height="591" alt="Screenshot_20260820_234255" src="https://github.com/user-attachments/assets/1b4993d4-a79d-400b-931c-709d0e2d6119" />
<img width="841" height="425" alt="Screenshot_20260820_234352" src="https://github.com/user-attachments/assets/76b1299d-863a-499d-b32d-4c46c7653b00" />

# BOM

Now then here should be everything required to make this yourself:

1. 12× Cherry MX Switches
2. 12× DSA Keycaps
3. 12× 1N4148 SOD-123 Diodes
4. 1× Xiao RP2040
5. 4× M2 × 6mm SHCS Bolts (Corner Screws)
6. Case (2 part case Top and Bottom)
7. Soldering iron + solder
8. Wire cutters
