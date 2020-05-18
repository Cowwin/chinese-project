#so this is the ranking system?
#hxt?
style inventory_label:
    xalign 0.2
style slot:
    background Frame("box", 0,0)
    minimum(80,80)
    maximum(80,80)
    xalign 0.5
screen info_screen(info_text):
    hbox:
        xalign 0.5
        yalign 0.5
        vbox:
            text "{color=#f0df26}{size=+10}[info_text]{/size}{/color}"
screen use_screen:
    hbox:
        xalign 0.1
        yalign 0.70
        vbox:
            textbutton "物品":
                action Show("inventory_screen")
screen inventory_screen:
    add Solid("#fffc")
    modal True
    hbox:
        xalign 0.5
        yalign 0.68

        grid 10 1:
            for item in inventory:
                frame:
                    style 'slot'
                    imagebutton idle item.img action SetVariable("selected_item", item)
            for i in range(len(inventory), 10):
                frame:
                    yalign 0.68
                    style 'slot'
    hbox:
        yalign 0.5
        xalign 0.5
        vbox:
            if selected_item != None:
                label selected_item.use
    textbutton "返回":
        xalign 0.15
        yalign 0.68
        action Hide("inventory_screen")
