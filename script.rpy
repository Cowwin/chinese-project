# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("余罪")
define pq = Character("许平秋")
define sb = Character("鼠标")
define sy = Character("孙羿")
define gwz = Character("瓜娃子")
define gs = Character("傅国生")
define wl = Character("阮磊")
define ab = Character("阿卜")
define hy = Character("豁牙")

init:
    $ style.default.font = "MaShanZheng-Regular.ttf"
    $ style.default.language = "eastasian"
# The game starts here.

label start:

    "从景泰派出所到白云看守所路程不短，几乎要横穿半个城区"
    "我坐在警车后厢的笼子里，突然听到了飞机的声音"
    "这条路我曾经来过，离机场的方向不远，连着西郊，初来乍到的时候，我几乎分不清这里的城市的乡村，因为到哪里都会有连幢的楼宇以及宽阔的马路"
    '这一切都不会再属于被剥夺“自由”的我了'
    "从宽路拐下一条废渣路，连绵的菜地、水塘、偶而呼啸而过的摩托车，带上了郊区的特征"
    "我长嗅一口气，觉得浑身疼痛加剧，忍不住冷生生地一个战栗"
    "我要去的地方是监狱"
    "高墙、铁窗、格子房"
    "那个未知的世界会有多少狰狞的恶汉？会有多少让人毛骨怵然的罪恶？"
    "这恐惧是我从来没有感觉过的"
    mc 'gay'

    return
