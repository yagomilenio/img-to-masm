class TranslateToMasm:
    def __init__(self, filename="out.asm"):
        self.f = open(filename, "w")
        self.f.write(".model small\n.stack\n.data\n.code\nmain PROC.\nmov ah,0\nmov al,13h\nint 10h\n")
       
        

    def translate(self, pixels, width=640, height=480):
        dx = 0
        cx = 0
        for i in pixels:
            if cx  == width:
                cx = 0
                dx +=1

                if dx == height:
                    exit

            self.f.write(f"\nmov cx,{cx}\nmov dx,{dx}\nmov al, {i}")
            cx +=1
                
    def finish(self):
        self.f.write(".exit\nmain ENDP\nend main")
        self.f.close()