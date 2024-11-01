#!/usr/bin/env python3

from bdfparser import Font

if __name__ == '__main__':
    
    #font = Font('unifont-13.0.04.bdf')
    font = Font('pris/PrisRegular-27.bdf')

    print(f"This font's global size is "
          f"{font.headers['fbbx']} x {font.headers['fbby']} (pixel), "
        f"it contains {len(font)} glyphs.")

    ac = font.glyph("a").draw().concat(
        font.glyph("c").draw()
    )
    #ac_8x8 = ac * 8
    
    from PIL import Image
    im_ac = Image.frombytes('RGBA',
                            (ac.width(), ac.height()),
                            ac.tobytes('RGBA'))
    im_ac.save("ac.png", "PNG")
    
