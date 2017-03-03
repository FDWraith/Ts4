from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 yrotate: create an y-axis rotation matrix,w
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 zrotate: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    with open(fname, "r") as file:
        line = file.readline().strip()
        while( line != "" and line != "quit"):
            cmd = line
            if cmd == "line":
                args = file.readline().strip()
                args = args.split(" ")
                if len(args) < 6:
                    print "Missing Args For Line"
                else:
                    add_edge( points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]) )
            elif cmd == "ident":
                ident( transform )
            elif cmd == "scale":
                args = file.readline().strip()
                args = args.split(" ")
                if len(args) < 3:
                    print "Missing Args For Scale"
                else:
                    scale = make_scale( int(args[0]), int(args[1]), int(args[2]) )
                    matrix_mult( scale, transform )
            elif cmd == "move":
                args = file.readline().strip()
                args = args.split(" ")
                if len(args) < 3:
                    print "Missing Args For Move"
                else:
                    move = make_translate( int(args[0]), int(args[1]), int(args[2]) )
                    matrix_mult( move, transform )
            elif cmd == "rotate":
                args = file.readline().strip()
                args = args.split(" ")
                if len(args) < 2:
                    print "Missing Args For Rotate"
                else:
                      if( args[0] == "x" ):
                          rotate = make_rotX( int(args[1]) )
                          matrix_mult( rotate, transform )
                      elif( args[0] == "y" ):
                          rotate = make_rotY( int(args[1]) )
                          matrix_mult( rotate, transform )
                      elif( args[0] == "z" ):
                          rotate = make_rotZ( int(args[1]) )
                          matrix_mult( rotate, transform )
                      else:
                          print "Axis not Found. We do not do Quantum Computing around here"
            elif cmd == "apply":
                matrix_mult( transform, points )
            elif cmd == "display":
                draw_lines( points, screen, color )
                display( screen )
            elif cmd == "save":
                args = line.readline().strip()
                if len(args) < 1:
                    print "All you had was one job. ONE JOB! And you couldn't even do that properly. We need a GODDAMN FILENAME to SAVE to! "
                else:
                    draw_lines( points, screen, color )
                    save_extension( screen, args[0])
            else:
                print "COMMAND NOT FOUND"
            line = file.readline().strip()
            
    
        
