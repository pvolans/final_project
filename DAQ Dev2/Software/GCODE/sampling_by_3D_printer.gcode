; Initialize Printer
G28 ; Home all axes
;G92 X110 Y110 Z0 ; Set current position to origin
M106 P0 S255 ;Extruder fan full 
M106 P1 S255 ;Enclosure fan full
M106 P2 S255 ;Auxiliarty fan full
M190 S35 ; Turn off bed 
M109 S30 ; Turn off extruder
;PAUSE

M140 S1 ; Turn off bed
M104 S1 ; Turn off extruder
M106 P0 S0 ;Extruder fan off
M106 P1 S0 ;Enclosure fan off
M106 P2 S0 ;Auxiliarty fan off

G90
M400

G1 X0 Y0 Z50 ; Set Zero pose X Y Z
M400
G4 P10000
;PAUSE ;Wait to start M703A script
G1 X100 Y0 Z50 ; Adjust the sample holder
M400
G4 P10000
G1 X5 Y5 Z50 ; Return Zero pose
M400
G91 ;Set relative positioning
G4 P13000 ; wait for the calibration process


;*****1 START*****

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400
;*****1 END*****

;Move 30mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y20 ; Move to (X, Y+5, Z)
M400

;*****2 START*****

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400
;*****2 END*****

;Move 30mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y20 ; Move to (X, Y+5, Z)
M400

;*****3 START*****

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400
;*****3 END*****

G90 ;Absolute position
G4 P140000 ;Wait for the last sample
G1 X55 Y5 ;go to the beginning of 4
M400
G91 ;Relative position

;*****4 START*****

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400
;*****4 END*****

;Move 30mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y20 ; Move to (X, Y+5, Z)
M400

;*****5 START*****

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400
;*****5 END*****

;Move 30mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y20 ; Move to (X, Y+5, Z)
M400

;*****6 START*****

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400
;*****6 END*****

G90 ;Absolute position
G4 P140000 ;Wait for the last sample
G1 X105 Y5 ;go to the beginning of 7
M400
G91 ;Relative position

;*****7 START*****

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400
;*****7 END*****

;Move 30mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y20 ; Move to (X, Y+5, Z)
M400

;*****8 START*****

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400
;*****8 END*****

;Move 30mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y20 ; Move to (X, Y+5, Z)
M400

;*****9 START*****

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Repeat this for 6 times (-5x6 = -30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X-5 Y0 ; Move to (X-5, Y+0, Z)
M400

;Move 5mm along Y-axis
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X0 Y5 ; Move to (X, Y+5, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400

;Repeat this for 6 times (5x6 = 30)
G4 P140000 ;Wait for 33.88sec to measure first sample
G1 X5 Y0 ; Move to (X+5, Y+0, Z)
M400
G4 P140000 
;*****9 END*****

; Finish
; G1 Z150 ; Raise nozzle
; M104 S0 ; Turn off extruder
; M140 S0 ; Turn off bed
; G28 ; Home all axes

END_PRINT ; Creality OS Function to finish gcode