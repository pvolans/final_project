G21 ; Set units to millimeters
G90 ; Use absolute positioning

G0 X0 Y0 ;Check the initial point
G4 P0


; --- Draw square (Laser on with movement) ---
M4
M100
G0 X100 Y0
G4 P0
G0 X100 Y100
G4 P0
G0 X0 Y100
G4 P0
G0 X0 Y0
; --- Draw square (Laser off with movement) ---
M5 ; Send the LASER control commands before next position for sync
M100
G4 P0
G0 X100 Y0
G4 P0
G0 X100 Y100
G4 P0
G0 X0 Y100
G4 P0
G0 X0 Y0

