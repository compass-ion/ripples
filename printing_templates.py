#  Templates for printing  #
# ======================== #

printing_template = {}

printing_template[2] = """
       +------------------------------------+
       |                                    |
       |        +----bbbbbbbbb----+         |
       |        |                 |         |
   eeeeeeeee    |    aaaaaaaaa    |     ddddddddd
       |        |                 |         |
       |        +----ccccccccc----+         |
       |                                    |
       +------------------------------------+
"""

printing_template[3] = """
    +-----------------iiiiiiiii-----------------+
    |                                           |
    |      +-----------------------------+      |
    |      |                             |      |
    |      |      +---bbbbbbbbb---+      |      |
    |  eeeeeeeee  |               |  fffffffff  |
    |      |      |   aaaaaaaaa   |      |      |
    |      |      |               |      |      |
    |      |  ddddddddd       ccccccccc  |      |
hhhhhhhhh  |      +---------------+      |  jjjjjjjjj
    |      |                             |      |
    |      +----------ggggggggg----------+      |
    |                                           |
    +-------------------------------------------+
"""

printing_template[4] = """
     +--------------------------ooooooooo--------------------------+
     |                                                             |
     |      jjjjjjjjj-------------------------------kkkkkkkkk      |
     |       |                                             |       |
     |       |      +-----------fffffffff-----------+      |       |
     |       |      |                               |      |       |
     |       |      |     eeeeeeeee---bbbbbbbbb     |      |       |
     |       |      |       |               |       |      |       |
 nnnnnnnnn   |  iiiiiiiii   |   aaaaaaaaa   |   ggggggggg  |   ppppppppp
     |       |      |       |               |       |      |       |
     |       |      |     ddddddddd---ccccccccc     |      |       |
     |       |      |                               |      |       |
     |       |      +-----------hhhhhhhhh-----------+      |       |
     |       |                                             |       |
     |      mmmmmmmmm-------------------------------lllllllll      |
     |                                                             |
     +--------------------------qqqqqqqqq--------------------------+
"""

printing_template[5] = """
       +--------------------------------------------xxxxxxxxxxxxx--------------------------------------------+
       |                                                                                                     |
       |      rrrrrrrrrrrrr---------------------------------------------------------------sssssssssssss      |
       |        |                                                                                   |        |
       |        |        +--------------------------mmmmmmmmmmmmm--------------------------+        |        |
       |        |        |                                                                 |        |        |
       |        |        |        +-ggggggggggggg-------------------hhhhhhhhhhhhh-+        |        |        |
       |        |        |        |                                               |        |        |        |
 wwwwwwwwwwwww  |        |        |          +------bbbbbbbbbbbbb------+          |        |        |  yyyyyyyyyyyyy
       |        |  lllllllllllll  |          |                         |          |  nnnnnnnnnnnnn  |        |
       |        |        |        |     fffffffffffff           ccccccccccccc     |        |        |        |
       |        |        |        |          |                         |          |        |        |        |
       |        |        |  kkkkkkkkkkkkk    |      aaaaaaaaaaaaa      |    iiiiiiiiiiiii  |        |        |
       |        |        |        |          |                         |          |        |        |        |
       |  qqqqqqqqqqqqq  |        |          |                         |          |        |  ttttttttttttt  |
       |        |        |        |        eeeeeeeeeeeee-----ddddddddddddd        |        |        |        |
       |        |        |        |                                               |        |        |        |
       |        |        |        +-----------------jjjjjjjjjjjjj-----------------+        |        |        |
       |        |        |                                                                 |        |        |
       |        |    ppppppppppppp-------------------------------------------------ooooooooooooo    |        |
       |        |                                                                                   |        |
       |        +-----------------------------------uuuuuuuuuuuuu-----------------------------------+        |
       |                                                                                                     |
   vvvvvvvvvvvvv-------------------------------------------------------------------------------------zzzzzzzzzzzzz
"""


if __name__ == "__main__":
    for key in printing_template:
        print(f"Printing Template for {key} ripples:")
        print(printing_template[key])
