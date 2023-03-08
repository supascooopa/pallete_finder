from colorthief import ColorThief
import webcolors


def color_grabber(image_file):

    color_thief = ColorThief(image_file)

    # build a color palette
    palette = color_thief.get_palette(color_count=10)
    # print(palette[0])
    hex_palette = [webcolors.rgb_to_hex(color_rgb) for color_rgb in palette]
    return hex_palette

