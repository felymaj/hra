babicka  = 159
deda = 1927692826382

while deda != babicka:
    if deda < babicka:
        deda += 1
        babicka -= 1
        print (" ODebral jsem babičce 1 a přidal 1 dědovi.")
        print ({babicka})
        print ({deda})
    else:
        deda -= 1
        babicka += 1
        print (" ODebral jsem dědovi 1 a přidal 1 babiččce.")
        print ({babicka})
        print ({deda})

