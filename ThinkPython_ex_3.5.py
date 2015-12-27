## ThinkPython Excercise 3.5
## creates a 4x4 grid.

def horizontals():
    print('+ - - - - + - - - - + - - - - + - - - - +')

def verticals():
    print('|' + (' ' * 9) + '|' + (' ' * 9) +'|' + (' ' * 9) +'|' + (' ' * 9) + '|')
##    verts =('|' + (' ' * 9) + '|' + (' ' * 9) +'|' + (' ' * 9) +'|' + (' ' * 9) + '|' + '\n')
##    print(verts  * 4)    

def grid():
    horizontals()
    verticals()
    verticals()
    verticals()
    verticals()
    horizontals()
    verticals()
    verticals()
    verticals()
    verticals()
    horizontals()
    verticals()
    verticals()
    verticals()
    verticals()
    horizontals()
    verticals()
    verticals()
    verticals()
    verticals()
    horizontals()
    
grid()
