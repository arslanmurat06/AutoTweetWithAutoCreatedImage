from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap
import glob
import jsonImporter

# pip install textwrap


def add_whatsapp_number_and_name(image_path, top_text, bottom_text, center_text):

    font = ImageFont.truetype('assets/Roboto-Medium.ttf', 50)
    im1 = Image.open(image_path)
    im2 = im1.filter(ImageFilter.GaussianBlur(radius=4))

    draw = ImageDraw.Draw(im2)

    image_width, image_height = im1.size
    stroke_width = 5
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()

    # text wrapping
    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    center_lines = textwrap.wrap(center_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

    # draw top lines
    y = 80
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font,
                  stroke_width=stroke_width, stroke_fill='black')
        y += line_height

    y = 150
    for line in center_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='white', font=font,
                  stroke_width=stroke_width, stroke_fill='black')
        y += line_height
        # draw bottom lines

    y = image_height - char_height * len(bottom_lines) - 250
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill='pink', font=font,
                  stroke_width=stroke_width, stroke_fill='black')
        y += line_height
    # im2.show()

    im2.save(im1.filename.replace('in', 'out'))


if __name__ == '__main__':
    center_text = "Whatsapp İhbar Hattı"
    list = glob.glob("DownloadedImages/in/*.*")
    nameList = jsonImporter.import_Data_From_Json_File()
    for index, value in enumerate(list):
        # print(value.replace('\\', '/') + "-" +
        #       nameList[index].name+"-"+nameList[index].number)
        add_whatsapp_number_and_name(
            value.replace('\\', '/'), top_text=nameList[index].name, bottom_text=nameList[index].number, center_text=center_text)
    print("completed")
