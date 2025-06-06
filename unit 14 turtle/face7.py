from turtle import *
from random import randint

speed(0)
hideturtle()


def myposition(x, y):
    penup()
    goto(x - 370, (y * -1) + 300)
    pendown()


def positions():
    positions.inner_dress = [(294, 421), (311, 470), (323, 501), (329, 529), (332, 541), (353, 534), (349, 509), (338, 476), (328, 461), (295, 422), (-1, -1), (432, 500), (450, 480), (473, 459), (512, 431), (530, 445), (515, 449), (498, 459), (485, 466), (459, 484), (444, 494), (433, 501),]
    
    positions.outer_dress = [(288, 403), (295, 423), (311, 442), (323, 454), (331, 463), (338, 472), (353, 534), (430, 503), (444, 487), (473, 458), (498, 435), (509, 427), (496, 415), (481, 391), (460, 436), (476, 380), (474, 347), (461, 375), (456, 388), (448, 398), (460, 389), (457, 400), (445, 427), (435, 440), (430, 449), (425, 461), (418, 472), (409, 475), (400, 475), (386, 469), (363, 456), (340, 441), (328, 435), (318, 426), (300, 413), (288, 403),]
    
    positions.extras = [(459, 438), (469, 411), (474, 394), (476, 370), (476, 354), (474, 330), (487, 322), (492, 335), (488, 346), (486, 351), (481, 354), (482, 366), (486, 388), (489, 397), (495, 414), (481, 392), (478, 401), (471, 417), (460, 438), (-1, -1), (240, 284), (237, 287), (231, 283), (229, 275), (230, 291), (235, 299), (240, 309), (241, 316), (244, 321), (251, 324), (247, 307), (242, 291), (240, 285),]
    
    positions.face_details = [(327, 366), (352, 366), (345, 371), (339, 371), (333, 371), (327, 367), (-1, -1), (301, 351), (305, 355), (313, 355), (323, 352), (331, 353), (340, 356), (348, 354), (353, 351), (360, 353), (366, 353), (373, 353), (380, 352), (387, 350), (389, 347), (385, 345), (378, 346), (372, 347), (363, 345), (352, 342), (346, 343), (337, 346), (332, 346), (328, 344), (323, 344), (316, 348), (309, 351), (301, 351), (-1, -1), (310, 301), (312, 312), (318, 316), (324, 314), (329, 312), (337, 316), (349, 320), (357, 317), (363, 315), (370, 314), (373, 308), (371, 297), (371, 303), (368, 309), (364, 304), (359, 300), (353, 300), (346, 304), (338, 307), (330, 307), (323, 304), (319, 301), (315, 304), (311, 302), (-1, -1), (363, 286), (361, 277), (356, 269), (354, 262), (355, 253), (360, 244), (367, 242), (375, 243), (382, 245), (395, 245), (379, 240), (384, 235), (394, 233), (394, 239), (399, 244), (406, 244), (410, 240), (417, 240), (413, 246), (407, 251), (390, 254), (406, 255), (413, 253), (420, 246), (423, 240), (430, 234), (423, 233), (416, 229), (408, 225), (401, 222), (393, 220), (407, 211), (417, 211), (427, 214), (439, 217), (434, 210), (423, 204), (416, 203), (400, 207), (382, 208), (367, 211), (357, 215), (348, 225), (352, 231), (352, 240), (352, 249), (350, 261), (349, 269), (352, 274), (358, 279), (363, 288), (363, 287), (-1, -1), (321, 229), (320, 234), (315, 244), (287, 249), (283, 244), (282, 240), (269, 247), (274, 250), (258, 248), (268, 240), (287, 231), (276, 228), (265, 226), (258, 226), (252, 227), (245, 230), (261, 219), (269, 219), (277, 221), (298, 213), (306, 217), (322, 229), (-1, -1), (282, 396), (303, 416), (320, 429), (335, 438), (365, 456), (384, 467), (404, 475), (416, 474), (422, 468), (426, 459), (431, 446), (441, 432), (448, 419), (457, 402), (459, 390), (447, 400), (454, 390), (462, 373), (473, 346), (467, 337), (462, 355), (455, 370), (450, 382), (441, 393), (427, 403), (413, 409), (397, 414), (389, 417), (374, 420), (357, 421), (343, 421), (330, 421), (322, 419), (314, 417), (304, 411), (282, 397),]
    
    positions.inner_face = [(328, 136), (320, 129), (305, 127), (296, 127), (290, 133), (281, 142), (272, 154), (266, 167), (264, 179), (264, 190), (263, 202), (260, 210), (261, 218), (245, 229), (251, 227), (256, 236), (256, 245), (251, 256), (250, 264), (249, 278), (251, 290), (256, 302), (261, 315), (266, 326), (268, 340), (272, 355), (278, 367), (285, 379), (289, 387), (297, 393), (312, 393), (310, 397), (308, 404), (310, 415), (322, 419), (342, 420), (355, 419), (367, 416), (376, 413), (384, 407), (389, 399), (387, 394), (379, 391), (373, 388), (365, 385), (355, 381), (345, 381), (337, 383), (319, 395), (330, 381), (340, 375), (352, 373), (366, 373), (378, 374), (387, 377), (403, 377), (411, 370), (417, 360), (423, 353), (431, 353), (440, 348), (442, 340), (447, 330), (449, 323), (449, 313), (448, 303), (454, 294), (457, 285), (457, 277), (457, 269), (455, 261), (449, 254), (444, 250), (437, 247), (428, 247), (416, 251), (422, 244), (424, 239), (431, 235), (426, 234), (419, 230), (409, 225), (401, 222), (392, 220), (403, 212), (411, 211), (416, 211), (440, 218), (436, 213), (430, 207), (421, 204), (421, 194), (421, 184), (427, 175), (433, 162), (433, 151), (431, 139), (425, 131), (418, 124), (408, 121), (397, 121), (384, 121), (375, 125), (362, 128), (352, 128), (341, 120), (346, 131), (336, 124), (322, 121), (327, 129), (329, 137),]
    
    positions.outer_face2 = [(x + randint(-6, 6), y + randint(-6, 6)) for (x, y) in [(350, 419), (363, 416), (377, 413), (385, 405), (388, 399), (385, 392), (376, 389), (366, 385), (355, 381), (346, 381), (339, 383), (331, 387), (321, 394), (325, 385), (336, 377), (349, 372), (363, 373), (372, 374), (383, 376), (391, 378), (401, 378), (408, 375), (413, 368), (422, 354), (430, 353), (438, 349), (443, 342), (446, 334), (448, 323), (449, 312), (448, 303), (454, 294), (457, 281), (457, 270), (454, 260), (449, 252), (441, 248), (428, 247), (418, 251), (424, 240), (430, 234), (425, 232), (417, 228), (404, 222), (391, 220), (405, 212), (415, 211), (425, 214), (439, 217), (433, 209), (422, 204), (420, 188), (395, 202), (420, 184), (423, 177), (409, 184), (425, 174), (430, 166), (432, 157), (434, 149), (431, 140), (426, 132), (419, 125), (406, 120), (418, 121), (427, 124), (434, 129), (440, 136), (443, 143), (450, 147), (458, 148), (453, 152), (455, 159), (456, 167), (453, 175), (458, 184), (451, 181), (457, 194), (464, 208), (469, 225), (473, 250), (473, 266), (471, 297), (469, 326), (465, 343), (458, 364), (452, 379), (444, 390), (433, 399), (418, 406), (407, 411), (393, 416), (379, 419), (366, 420), (351, 420)]]
    
    positions.outer_face = [(x + randint(-2, 2), y + randint(-2, 2)) for (x, y) in [(243, 199), (241, 205), (240, 219), (240, 229), (240, 243), (240, 264), (240, 278), (244, 294), (248, 310), (251, 322), (254, 339), (256, 347), (264, 369), (271, 384), (276, 391), (289, 400), (296, 406), (303, 411), (311, 416), (318, 419), (329, 421), (343, 420), (350, 420), (360, 420), (369, 420), (379, 419), (394, 416), (406, 412), (414, 409), (425, 405), (435, 398), (442, 393), (447, 386), (452, 379), (456, 370), (460, 359), (465, 347), (466, 336), (469, 326), (470, 308), (472, 289), (473, 273), (473, 253), (471, 236), (467, 218), (463, 205), (458, 196), (450, 182), (457, 183), (454, 176), (456, 165), (453, 153), (457, 149), (450, 149), (445, 144), (440, 137), (434, 130), (425, 123), (412, 119), (401, 119), (389, 121), (379, 123), (368, 127), (361, 128), (353, 128), (341, 120), (345, 132), (322, 121), (329, 135), (317, 129), (304, 126), (291, 129), (281, 132), (274, 139), (268, 145), (260, 161), (261, 150), (269, 134), (258, 143), (253, 152), (250, 162), (249, 171), (249, 182), (250, 194), (250, 205), (247, 213), (244, 219), (244, 213), (245, 206), (243, 200)]]
    
    positions.hair_details = [(311, 122), (295, 120), (280, 122), (263, 126), (221, 155), (239, 135), (249, 128), (278, 118), (266, 118), (254, 121), (238, 129), (216, 149), (229, 133), (246, 120), (269, 112), (256, 112), (246, 114), (225, 125), (243, 112), (258, 108), (272, 106), (288, 107), (297, 110), (276, 110), (289, 112), (299, 116), (311, 123), (-1, -1), (326, 117), (317, 105), (306, 84), (296, 64), (287, 53), (284, 50), (266, 41), (281, 52), (290, 61), (298, 74), (305, 87), (313, 101), (326, 118), (-1, -1), (303, 97), (295, 90), (286, 79), (279, 68), (271, 59), (262, 53), (256, 51), (263, 56), (270, 64), (275, 71), (281, 79), (287, 86), (296, 94), (304, 98), (-1, -1), (331, 58), (329, 52), (325, 46), (321, 40), (305, 30), (316, 34), (324, 39), (328, 46), (334, 55), (345, 67), (341, 60), (338, 53), (330, 37), (338, 42), (345, 48), (348, 56), (352, 66), (356, 76), (359, 97), (360, 86), (356, 64), (352, 53), (347, 44), (343, 38), (336, 32), (322, 29), (322, 34), (306, 26), (295, 24), (281, 25), (264, 29), (280, 28), (293, 28), (300, 33), (311, 38), (320, 46), (332, 58), (-1, -1), (364, 83), (366, 69), (365, 58), (363, 54), (362, 48), (356, 38), (346, 30), (352, 38), (335, 29), (343, 36), (352, 48), (357, 57), (361, 66), (364, 84), (-1, -1), (384, 89), (382, 77), (380, 65), (385, 54), (387, 48), (389, 41), (396, 30), (396, 37), (395, 39), (390, 50), (386, 56), (385, 62), (384, 71), (385, 91), (-1, -1), (396, 86), (394, 76), (396, 64), (400, 52), (406, 43), (405, 33), (408, 38), (406, 46), (403, 52), (400, 59), (398, 66), (397, 73), (396, 87), (-1, -1), (414, 74), (416, 61), (416, 53), (416, 46), (414, 36), (418, 38), (421, 45), (421, 51), (419, 58), (415, 74), (-1, -1), (415, 103), (425, 93), (446, 88), (432, 94), (453, 95), (473, 100), (484, 107), (495, 116), (503, 124), (511, 144), (506, 135), (500, 125), (481, 110), (496, 123), (501, 133), (504, 150), (503, 163), (496, 175), (501, 160), (502, 148), (498, 135), (485, 117), (493, 131), (494, 151), (487, 168), (472, 185), (489, 161), (490, 141), (483, 125), (475, 117), (452, 107), (464, 114), (469, 121), (458, 116), (444, 112), (432, 109), (417, 112), (425, 107), (441, 105), (459, 107), (474, 114), (452, 104), (437, 103), (427, 105), (444, 101), (463, 104), (449, 99), (439, 99), (424, 103), (418, 108), (429, 97), (416, 103),]
    
    positions.hair = [(x + randint(-2, 2), y + randint(-2, 2)) for (x, y) in [(239, 281), (229, 254), (224, 258), (227, 246), (219, 230), (213, 207), (212, 194), (215, 181), (210, 185), (210, 173), (212, 160), (207, 171), (208, 186), (203, 174), (204, 165), (208, 154), (207, 146), (203, 136), (203, 125), (206, 112), (200, 112), (192, 105), (198, 106), (209, 106), (203, 102), (199, 94), (202, 86), (203, 89), (204, 94), (212, 95), (208, 91), (209, 87), (211, 91), (218, 91), (222, 87), (226, 77), (221, 75), (216, 70), (214, 61), (204, 68), (213, 53), (197, 74), (207, 53), (227, 33), (236, 27), (248, 22), (259, 18), (272, 15), (283, 15), (298, 14), (308, 16), (318, 18), (330, 21), (337, 21), (336, 17), (336, 9), (339, 15), (347, 14), (357, 11), (368, 8), (382, 10), (379, 6), (398, 17), (390, 3), (409, 22), (410, 15), (415, 8), (422, 8), (416, 13), (416, 21), (418, 29), (428, 35), (434, 43), (441, 53), (445, 63), (444, 71), (458, 67), (468, 69), (478, 81), (473, 75), (463, 72), (454, 73), (451, 78), (460, 74), (457, 82), (469, 86), (462, 87), (483, 95), (480, 98), (493, 99), (505, 105), (513, 113), (518, 120), (521, 137), (518, 131), (513, 123), (518, 139), (520, 150), (519, 164), (520, 177), (523, 183), (529, 190), (522, 190), (516, 208), (512, 225), (516, 231), (521, 236), (523, 245), (523, 258), (520, 274), (514, 290), (506, 306), (504, 316), (503, 325), (500, 336), (494, 350), (490, 346), (487, 350), (483, 355), (474, 346), (464, 343), (468, 327), (473, 273), (471, 240), (468, 219), (461, 203), (449, 181), (458, 183), (453, 176), (454, 168), (454, 161), (452, 153), (456, 149), (449, 147), (444, 141), (437, 132), (429, 125), (419, 121), (410, 119), (397, 119), (386, 122), (376, 124), (365, 128), (358, 128), (351, 126), (340, 120), (346, 130), (338, 126), (328, 122), (322, 121), (327, 128), (329, 135), (319, 128), (305, 125), (293, 127), (282, 132), (273, 139), (267, 147), (259, 159), (263, 147), (270, 133), (264, 138), (255, 147), (252, 155), (250, 164), (249, 176), (250, 187), (250, 195), (250, 202), (248, 211), (242, 219), (244, 211), (243, 196), (240, 205), (240, 281)]]
    
    positions.left_ear = [(240, 282), (234, 269), (228, 254), (224, 259), (225, 247), (217, 255), (214, 264), (217, 276), (224, 288), (227, 302), (231, 313), (236, 325), (243, 334), (252, 334), (248, 313), (243, 295), (241, 283),]
    
    positions.line = [(335, 550), (412, 526), (432, 517), (454, 503), (467, 493), (488, 475), (509, 463), (567, 443), (537, 453), (516, 463), (495, 476), (477, 491), (464, 500), (440, 516), (416, 530), (388, 541), (365, 548), (361, 550), (335, 551),]
    
    positions.nose = [(311 + randint(-2, 2), 221 + randint(-2, 2)), (317 + randint(-2, 2), 223 + randint(-2, 2)), (331 + randint(-2, 2), 224 + randint(-2, 2)), (339 + randint(-2, 2), 230 + randint(-2, 2)), (341 + randint(-2, 2), 246 + randint(-2, 2)), (339 + randint(-2, 2), 252 + randint(-2, 2)), (337 + randint(-2, 2), 262 + randint(-2, 2)), (339 + randint(-2, 2), 272 + randint(-2, 2)), (344 + randint(-2, 2), 285 + randint(-2, 2)), (347 + randint(-2, 2), 292 + randint(-2, 2)), (346 + randint(-2, 2), 297 + randint(-2, 2)), (340 + randint(-2, 2), 302 + randint(-2, 2)), (333 + randint(-2, 2), 305 + randint(-2, 2)), (327 + randint(-2, 2), 301 + randint(-2, 2)), (321 + randint(-2, 2), 293 + randint(-2, 2)), (320 + randint(-2, 2), 288 + randint(-2, 2)), (322 + randint(-2, 2), 278 + randint(-2, 2)), (326 + randint(-2, 2), 267 + randint(-2, 2)), (324 + randint(-2, 2), 261 + randint(-2, 2)), (322 + randint(-2, 2), 252 + randint(-2, 2)), (320 + randint(-2, 2), 240 + randint(-2, 2)), (320 + randint(-2, 2), 236 + randint(-2, 2)), (321 + randint(-2, 2), 230 + randint(-2, 2)), (318 + randint(-2, 2), 227 + randint(-2, 2)), (311 + randint(-2, 2), 222 + randint(-2, 2))]

    positions.dress_lines = [(326, 428), (340, 467), (347, 492), (354, 533), (-1, -1), (390, 520), (386, 499), (378, 464), (-1, -1), (426, 457), (430, 469), (440, 496), (-1, -1), (483, 464), (475, 455), (469, 444), (462, 425), (455, 407), (-1, -1), (300, 436), (310, 432), (327, 433), (-1, -1), (313, 469), (322, 465), (340, 468), (358, 462), (377, 465), (-1, -1), (434, 442), (447, 432), (462, 426), (471, 414), (488, 402), (-1, -1), (510, 430), (494, 437), (482, 448), (476, 455), (464, 460), (453, 464), (446, 470), (434, 482), (419, 486), (409, 487), (401, 490), (387, 500), (377, 498), (369, 498), (349, 504), (341, 503), (335, 503), (325, 503), (-1, -1), (461, 376), (468, 371), (476, 369)]


def color_fill(coordinates, co = (0, 0, 0)):
    color(co)
    p_x, p_y = coordinates[0]
    myposition(p_x, p_y)
    fillcolor(co)
    begin_fill()
    t = 0
    for i in coordinates[1:]:
        x, y = i
        if t:
            myposition(x, y)
            t = 0
            begin_fill()
            continue
            
        if x == -1 and y == -1:
            t = 1
            end_fill()
            continue
        else:
            goto(x - 370, (y * -1) + 300)
    end_fill()


def draw(coordinates, mode = 1, co = (0, 0, 0), thickness = 1):
    co = (co[0] / 255, co[1] / 255, co[2] / 255)
    color(co)
    
    if mode:
        width(thickness)
        p_x, p_y = coordinates[0]
        myposition(p_x, p_y)
        t = 0
        for i in coordinates[1:]:
            x, y = i
            if t:
                myposition(x, y)
                t = 0
                continue
            if x == -1 and y == -1:
                t = 1
                continue
            else:
                goto(x - 370, (y * -1) + 300)
    else:
        color_fill(coordinates, co)


def files():
    positions()
    draw(positions.outer_face, co = (randint(203,217), randint(172,179), randint(130,169)), mode = 0)
    draw(positions.inner_face, co = (randint(218,222), randint(127,150), randint(102,160)), mode = 0)
    draw(positions.left_ear, co = (77, 77, 77), mode = 0)
    draw(positions.outer_face2, co = (77, 77, 77), mode = 0)
    draw(positions.face_details, mode = 0)
    draw(positions.nose, co = (204, 204, 204), mode = 0)
    draw(positions.outer_dress, co = (201, 0, 15), mode = 0)
    draw(positions.inner_dress, co = (230, 30, 36), mode = 0)
    draw(positions.hair, mode = 0)
    draw(positions.extras, mode = 0)
    draw(positions.hair_details, thickness = 1, co = (128, 128, 128), mode = 0)
    draw(positions.dress_lines, thickness = 5, mode = 1)
    draw(positions.line, mode = 0, co = (198, 0, 15))
    
    
files()
done()