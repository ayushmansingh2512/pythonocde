def look_for_the_key(box):
    for item in box:
        if isinstance(item,list):
            look_for_the_key(item)
        elif item == "key":
            print("Found the key")

boxes = ["item1", ["item2", ["key", "item3"]], "item4"]

look_for_the_key(boxes)
