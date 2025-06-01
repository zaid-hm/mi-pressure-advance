
    G28
    M104 S180; preheat nozzle while waiting for build plate to get to temp
    M190 S60;
    G28 Z
    M109 S220;
    
        G21 ; Millimeter units
        G90 ; Absolute XYZ
        M83 ; Relative E
        SET_VELOCITY_LIMIT ACCEL=3000 ACCEL_TO_DECEL=1500
        G92 E0 ;
        M106 S0 ; set fan speed to 0

        G1 X60.4 Y25.6 Z20 F30000 ; move to start position
        G1 Z0.25 F300 ; move to layer height
        G91 ; switch to relative movements

        ; Print a bounding box to aid with removal and prime the extruder.
        G1 E1.0
        G1 Y44.8 E2.0562752 F2000;
        G1 X-30.8 E1.4136892 F2000;
        G1 Y-44.8 E2.0562752 F2000;
        G1 X30.8 E1.4136892 F2000;
        G1 X-0.4 Y0.4
        ; second bounding box loop
        G1 Y44 E2.019556 F2000;
        G1 X-30 E1.37697 F2000;
        G1 Y-44 E2.019556 F2000;
        G1 X30 E1.37697 F2000;

        G1 Z0.75 E-0.5 F300; retract and prepare to hop to first line location.
    
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
    G1 Z5; move up 1mm
    M117
    
        G90; switch back to absolute coordinates
        G1 X30 Y200 Z20 F30000;
        
        G21 ; Millimeter units
        G90 ; Absolute XYZ
        M83 ; Relative E
        SET_VELOCITY_LIMIT ACCEL=3000 ACCEL_TO_DECEL=1500
        G92 E0 ;
        M106 S0 ; set fan speed to 0

        G1 X95.4 Y25.6 F30000 ; move to start position
        G1 Z0.25 F300 ; move to layer height
        G91 ; switch to relative movements

        ; Print a bounding box to aid with removal and prime the extruder.
        G1 E1.0
        G1 Y44.8 E2.0562752 F2000;
        G1 X-30.8 E1.4136892 F2000;
        G1 Y-44.8 E2.0562752 F2000;
        G1 X30.8 E1.4136892 F2000;
        G1 X-0.4 Y0.4
        ; second bounding box loop
        G1 Y44 E2.019556 F2000;
        G1 X-30 E1.37697 F2000;
        G1 Y-44 E2.019556 F2000;
        G1 X30 E1.37697 F2000;

        G1 Z0.75 E-0.5 F300; retract and prepare to hop to first line location.
    
            SET_PRESSURE_ADVANCE ADVANCE=0.0 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.0
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.006666666666666666 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.006666666666666666
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.013333333333333332 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.013333333333333332
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.019999999999999997 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.019999999999999997
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.026666666666666665 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.026666666666666665
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.03333333333333333 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.03333333333333333
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.039999999999999994 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.039999999999999994
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.04666666666666666 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04666666666666666
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.05333333333333333 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.05333333333333333
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.06 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.06
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
    G1 Z5; move up 1mm
    M117
    
        G90; switch back to absolute coordinates
        G1 X30 Y200 Z20 F30000;
        
        G21 ; Millimeter units
        G90 ; Absolute XYZ
        M83 ; Relative E
        SET_VELOCITY_LIMIT ACCEL=3000 ACCEL_TO_DECEL=1500
        G92 E0 ;
        M106 S0 ; set fan speed to 0

        G1 X130.4 Y25.6 F30000 ; move to start position
        G1 Z0.25 F300 ; move to layer height
        G91 ; switch to relative movements

        ; Print a bounding box to aid with removal and prime the extruder.
        G1 E1.0
        G1 Y44.8 E2.0562752 F2000;
        G1 X-30.8 E1.4136892 F2000;
        G1 Y-44.8 E2.0562752 F2000;
        G1 X30.8 E1.4136892 F2000;
        G1 X-0.4 Y0.4
        ; second bounding box loop
        G1 Y44 E2.019556 F2000;
        G1 X-30 E1.37697 F2000;
        G1 Y-44 E2.019556 F2000;
        G1 X30 E1.37697 F2000;

        G1 Z0.75 E-0.5 F300; retract and prepare to hop to first line location.
    
            SET_PRESSURE_ADVANCE ADVANCE=0.04 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.04 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.04 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.04 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.04 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.04 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.04 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.04 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.04 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
            SET_PRESSURE_ADVANCE ADVANCE=0.04 ; set Pressure Advance
            M117 Testing Pressure Advance at: 0.04
            G1 X-30 Y4 F30000        ; move to start position
            G1 Z-0.75 F300           ; move to layer height
            G1 E0.5 F1800           ; un-retract
            G1 X7.5 E0.3442425 F300     ; print line part one
            G1 X15.0 E0.688485 F9000    ; print line part two
            G1 X7.5 E0.3442425 F300     ; print line part three
            G1 E-0.5 F1800          ; retract
            G1 Z0.75 F300            ; Move above layer height 
        
    G1 Z5; move up 1mm
    M117
    
        G90; switch back to absolute coordinates
        G1 X30 Y200 Z20 F30000;
        
    SET_PRESSURE_ADVANCE ADVANCE=0.04
    