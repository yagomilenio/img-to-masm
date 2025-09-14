from pixel import PixelGroup

class TranslateToMasm:
    def __init__(self, filename="out.asm"):
        self.f = open(filename, "w")
        self.f.write(".model small\n.stack\n.data\n.code\nmain PROC\nmov ah,0\nmov al,13h\nint 10h\nmov ah, 0Ch\nmov bh, 0\n")
       
    def optimize(self, pixels):
        procesedList = []
        i = 0
        while i < len(pixels):
            p = pixels[i]
            repeats = 1

            while (i + repeats < len(pixels) and
                p.color == pixels[i + repeats].color and
                p.y == pixels[i + repeats].y):
                repeats += 1


            procesedList.append(PixelGroup(p.color, p.x, p.y, repeats))
            i += repeats
        return procesedList
        
    def translate(self, pixels):
    
        for p in pixels:
            if p.repeats == 1:
                # un solo pixel
                if p.color != 0:    #si es negro ya no aplica nada
                    self.f.write(f"\nmov cx,{p.x}\nmov dx,{p.y}\nmov al,{p.color}\nint 10h")
            else:
                # grupo de píxeles consecutivos en horizontal
                if p.color !=0:
                    self.f.write(f"""
    mov cx,{p.x}
    mov dx,{p.y}
    mov al,{p.color}
    mov bx,{p.repeats}
    loop_p_{p.y}_{p.x}:
    int 10h
    inc cx
    dec bx
    jnz loop_p_{p.y}_{p.x}
    """)

                
    def finish(self):
        self.f.write("\nmov ah, 0\nint 16h\n.exit\nmain ENDP\nend main")
        self.f.close()