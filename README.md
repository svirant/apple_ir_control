# apple_ir_control

This was inspired by a thread about controlling Moode Audio with an Apple IR remote without the use of LIRC. http://moodeaudio.org/forum/showthread.php?tid=3584

My version is stripped down and depends heavily on piir: https://pypi.org/project/PiIR/ It's currently setup so a single Apple remote can not only control Moode but also a few other IR devices when Moode is in a stopped state.

Usage: python3 apple_ir_control.py
or
Test mode: python3 apple_ir_control.py test

Test mode allows you to see the data that is returned on keypress.  From this you can copy out the 'data' part that is unique and use it for button press matches.
