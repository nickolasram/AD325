from simpleTextEditor import TextEditor


def test_editor():
    test1 = TextEditor()  # simple test
    test1.addText("s")
    assert test1.retrieveText() == "s"
    test1.addText("h")
    assert test1.retrieveText() == "sh"
    test1.undo()
    assert test1.retrieveText() == "s"
    test1.addText("h")
    assert test1.retrieveText() == "sh"
    test1.addText("h")
    assert test1.retrieveText() == "shh"
    test1.delete()
    assert test1.retrieveText() == "sh"
    test1.undo()
    assert test1.retrieveText() == "shh"
    test1.undo()
    assert test1.retrieveText() == "sh"

    test2 = TextEditor()  # testing for over deletion
    test2.addText("a")
    assert test2.retrieveText() == "a"
    test2.delete()
    assert test2.retrieveText() == ""
    test2.delete()
    assert test2.retrieveText() == ""

    test3 = TextEditor()  # testing for over undoing
    test3.addText("a")
    assert test3.retrieveText() == "a"
    test3.undo()
    assert test3.retrieveText() == ""
    test3.undo()
    assert test3.retrieveText() == ""

    test4 = TextEditor()
    goal = "decorum which might have been expected. Legs, leaning against the wall near"
    goal_typos1 = "decorummm"
    goal_typos2 = " which might have been expected. "
    goal_typos3 = "Legs, leaning against the wall near"
    for i in goal_typos1:
        test4.addText(i)
    test4.delete()
    test4.delete()
    for i in goal_typos2:
        test4.addText(i)
    test4.delete()
    test4.undo()
    test4.addText(".")
    test4.undo()
    for i in goal_typos3:
        test4.addText(i)
    assert test4.retrieveText() == goal, test4.retrieveText()
    print("NO ERRORS FOUND.")


test_editor()
