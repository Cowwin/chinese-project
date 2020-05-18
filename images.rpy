image diary:
    "/images/book.jpg"
    size(80,80)
image box:
    "/images/box.png"
    size(80,80)
image mystery = ConditionSwitch("_last_say_who == 'sr'", "/images/mystery.png",
                                "not _last_say_who == 'sr'", im.MatrixColor("/images/mystery.png", im.matrix.brightness(-0.5)))
