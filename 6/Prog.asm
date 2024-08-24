// This program runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen, namely, writes “black” in every pixel.
// When no key is pressed, the screen should be cleared. You may choose to blacken and clear the screen in
// any spatial order, as long as pressing a key continuously for long enough will result in a fully blackened
// screen and not pressing any key for long enough will result in a cleared screen. This program has a test
// script (Fill.tst) but no compare file—it should be checked by visibly inspecting the simulated screen.
(LOOP_KEYBOARD)
    @24575  // Last pixel cell - bottom right of the screen
    D=A
    @i     // Set 24575 as start value of i
    M=D
    @KBD
    D=M
    @LOOP_SCREEN_BLACK
    D;JGT   // If a key is pressed, D would be != 0
    @LOOP_SCREEN_WHITE
    0;JMP

(LOOP_SCREEN_BLACK)
    @i
    A=M
    M=-1    // Blank the cell of position i
    @i
    M=M-1   // Decrement i
    D=M
    @SCREEN // Index of first pixel - top left of the screen
    D=D-A   // Calculate i - first cell, if < 0 it means i reached all the pixels and exit the loop
    @LOOP_SCREEN_BLACK
    D;JGE
    @LOOP_KEYBOARD
    0;JMP

(LOOP_SCREEN_WHITE)
    @i
    A=M
    M=0    // Clear the cell of position i
    @i
    M=M-1   // Decrement i
    D=M
    @SCREEN // Index of first pixel - top left of the screen
    D=D-A   // Calculate i - first cell, if < 0 it means i reached all the pixels and exit the loop
    @LOOP_SCREEN_WHITE
    D;JGE
    @LOOP_KEYBOARD
    0;JMP